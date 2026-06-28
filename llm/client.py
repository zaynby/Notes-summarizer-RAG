import logging
import httpx
import config

log = logging.getLogger("llm")

NIM_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def chat(system_prompt: str, user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer {config.NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": config.LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "temperature": 0.2,
        "max_tokens": 2048,
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
