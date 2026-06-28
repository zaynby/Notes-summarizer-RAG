import asyncio
import logging
from collections import defaultdict
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import config
from rag.retriever import query as kb_query
from llm.client import chat, classify_intent

log = logging.getLogger("bot")

MAX_HISTORY = 20

conversations: dict = defaultdict(list)

SYSTEM_SEARCH = """You are a study assistant. Answer the user's question using the provided notes. If the notes don't contain enough information, say so. Cite the source file and slide/page number.

Notes:
{notes}"""

SYSTEM_SUMMARIZE = """You are a study assistant. Provide a comprehensive summary of the user's notes on the requested topic using the notes below. Organize it clearly with key points and concepts. If the notes aren't enough, say so.

Notes:
{notes}"""

SYSTEM_CHAT = "You are a helpful study assistant. Answer naturally based on the conversation history."


async def start(update: Update, context):
    user_id = update.effective_user.id
    conversations[user_id].clear()
    await update.message.reply_text(
        "Study Bot ready! I can answer questions, summarize notes, or just chat.\n\n"
        "/clear - Reset conversation"
    )


async def clear(update: Update, context):
    user_id = update.effective_user.id
    conversations[user_id].clear()
    await update.message.reply_text("Conversation reset.")


def _build_history(user_id: int, count: int = 6):
    msgs = conversations[user_id]
    return msgs[-(count + 1):-1] if len(msgs) > count + 1 else msgs[:-1]


async def handle_message(update: Update, context):
    user_id = update.effective_user.id
    text = update.message.text.strip()
    if not text:
        return

    await update.message.reply_chat_action("typing")
    conversations[user_id].append({"role": "user", "content": text})

    loop = asyncio.get_event_loop()

    try:
        intent = await loop.run_in_executor(None, classify_intent, conversations[user_id])

        if intent["type"] == "chat":
            hist = conversations[user_id][-6:]
            answer = await loop.run_in_executor(
                None, chat,
                [{"role": "system", "content": SYSTEM_CHAT}] + hist
            )

        elif intent["type"] == "summarize":
            results = await loop.run_in_executor(None, kb_query, intent["query"], 20, None) or []
            if results:
                notes_block = "\n\n".join(
                    f"[{r['filename']} - {r['label']}]\n{r['text']}" for r in results
                )
                answer = await loop.run_in_executor(
                    None, chat,
                    [
                        {"role": "system", "content": SYSTEM_SUMMARIZE.format(notes=notes_block)},
                        {"role": "user", "content": f"Summarize the notes on: {intent['query']}"},
                    ]
                )
                if answer:
                    sources = "\n\nSources:\n" + "\n".join(
                        f"• {r['filename']} ({r['label']})" for r in results[:5]
                    )
                    answer += sources
            else:
                answer = "I couldn't find any notes on that topic to summarize."

        else:
            results = await loop.run_in_executor(None, kb_query, intent["query"], 5, None) or []
            if not results:
                hist = conversations[user_id][-6:]
                answer = await loop.run_in_executor(
                    None, chat,
                    [{"role": "system", "content": SYSTEM_CHAT}] + hist
                )
            else:
                notes_block = "\n\n".join(
                    f"[{r['filename']} - {r['label']}]\n{r['text']}" for r in results
                )
                hist = _build_history(user_id, 4)
                answer = await loop.run_in_executor(
                    None, chat,
                    [
                        {"role": "system", "content": SYSTEM_SEARCH.format(notes=notes_block)},
                        *hist,
                        {"role": "user", "content": text},
                    ]
                )
                if answer:
                    sources = "\n\nSources:\n" + "\n".join(
                        f"• {r['filename']} ({r['label']})" for r in results[:3]
                    )
                    answer += sources

        if not answer:
            answer = "I couldn't generate a response. Please try again."

        conversations[user_id].append({"role": "assistant", "content": answer})
        if len(conversations[user_id]) > MAX_HISTORY:
            conversations[user_id] = conversations[user_id][-MAX_HISTORY:]

        if len(answer) > 4000:
            for i in range(0, len(answer), 4000):
                await update.message.reply_text(answer[i:i + 4000])
        else:
            await update.message.reply_text(answer)

    except Exception as e:
        log.error(f"Error handling message: {e}", exc_info=True)
        await update.message.reply_text("Something went wrong. Try again.")


def run_bot():
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    log.info("Starting Telegram bot...")
    app.run_polling()
