import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import config
from rag.retriever import query as kb_query
from llm.client import chat

log = logging.getLogger("bot")

SYSTEM_PROMPT = """You are a study assistant. Answer the question using ONLY the provided notes. If the notes don't contain enough information, say so clearly. Cite the source file and slide/page number for each point.

Notes:
{notes}

Question: {question}"""

async def start(update: Update, context):
    await update.message.reply_text(
        "Study Bot ready. Send me any question about your course materials."
    )

async def handle_message(update: Update, context):
    question = update.message.text.strip()
    if not question:
        return

    await update.message.reply_text("Searching your notes...")

    loop = asyncio.get_event_loop()
    try:
        results = await loop.run_in_executor(None, kb_query, question, 5, None)
        if not results:
            await update.message.reply_text("No relevant notes found.")
            return

        notes_block = "\n\n".join(
            f"[{r['filename']} - {r['label']}]\n{r['text']}"
            for r in results
        )

        answer = await loop.run_in_executor(
            None, chat,
            SYSTEM_PROMPT.format(notes=notes_block, question=question),
            "Provide your answer based on the notes above."
        )

        if not answer:
            await update.message.reply_text("Could not generate an answer.")
            return

        sources = "\n\nSources:\n" + "\n".join(
            f"• {r['filename']} ({r['label']})" for r in results[:3]
        )
        reply = answer + sources

        if len(reply) > 4000:
            for i in range(0, len(reply), 4000):
                await update.message.reply_text(reply[i:i + 4000])
        else:
            await update.message.reply_text(reply)

    except Exception as e:
        log.error(f"Error handling message: {e}")
        await update.message.reply_text("Something went wrong. Try again.")

def run_bot():
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    log.info("Starting Telegram bot...")
    app.run_polling()
