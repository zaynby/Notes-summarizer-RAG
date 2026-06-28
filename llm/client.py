import logging
import httpx
import config

log = logging.getLogger("llm")

NIM_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def chat(messages: list, temperature: float = 0.2, max_tokens: int = 2048) -> str:
    headers = {
        "Authorization": f"Bearer {config.NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": config.LLM_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    try:
        resp = httpx.post(NIM_API_URL, headers=headers, json=body, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except httpx.HTTPStatusError as e:
        log.error(f"NVIDIA API error {e.response.status_code}: {e.response.text}")
        return ""
    except Exception as e:
        log.error(f"LLM call failed: {e}")
        return ""

def classify_intent(messages: list) -> dict:
    history_lines = []
    for msg in messages[-6:]:
        role = "User" if msg["role"] == "user" else "Assistant"
        content = msg["content"][:200]
        history_lines.append(f"{role}: {content}")
    history_str = "\n".join(history_lines)

    system_prompt = (
        "You are an intent classifier for a study assistant. "
        "Given the conversation and the latest user message, output exactly one line:\n\n"
        "- If the user needs information from their notes: SEARCH: <optimized query>\n"
        "- If the user wants a summary of their notes on a topic: SUMMARIZE: <topic>\n"
        "- If the user is just chatting or asking a follow-up answerable from conversation: CHAT\n\n"
        "Examples:\n"
        "User: What is backpropagation?\n"
        "SEARCH: backpropagation neural networks\n\n"
        "User: Tell me more\n"
        "CHAT\n\n"
        "User: Summarize the machine learning notes\n"
        "SUMMARIZE: machine learning\n\n"
        "Conversation:\n"
        f"{history_str}\n\n"
        "Output:"
    )

    result = chat([
        {"role": "system", "content": system_prompt},
    ], temperature=0.0, max_tokens=100).strip()

    if result.upper().startswith("SEARCH:"):
        query = result[len("SEARCH:"):].strip()
        return {"type": "search", "query": query or messages[-1]["content"]}
    elif result.upper().startswith("SUMMARIZE:"):
        topic = result[len("SUMMARIZE:"):].strip()
        return {"type": "summarize", "query": topic or messages[-1]["content"]}
    else:
        return {"type": "chat"}
