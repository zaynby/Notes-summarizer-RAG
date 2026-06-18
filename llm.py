import time
import requests
from typing import Optional, Dict, Any
import config

def _call_nvidia(prompt: str, system: str = "", max_retries: int = 1) -> str:
    headers = {
        "Authorization": f"Bearer {config.NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": config.NVIDIA_MODEL,
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 4096,
    }

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{config.NVIDIA_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=120,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt < max_retries:
                time.sleep(5)
                continue
            return f"[NVIDIA API Error: {str(e)}]"

def _call_ollama(prompt: str, system: str = "", max_retries: int = 1) -> str:
    try:
        import ollama
        client = ollama.Client(host=config.OLLAMA_BASE_URL)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = client.chat(
            model=config.OLLAMA_MODEL,
            messages=messages,
            options={"temperature": 0.5, "num_predict": 4096},
        )
        return response["message"]["content"]
    except Exception as e:
        return f"[Ollama Error: {str(e)}]"

def _call_openrouter(prompt: str, system: str = "", max_retries: int = 1) -> str:
    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": "Personal Agent",
    }
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": config.OPENROUTER_MODEL,
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 4096,
    }

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{config.OPENROUTER_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=120,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt < max_retries:
                time.sleep(5)
                continue
            return f"[OpenRouter Error: {str(e)}]"

def call_llm(prompt: str, system: str = "", provider: Optional[str] = None) -> str:
    "Call the configured LLM provider. Falls back to next provider on error."
    prov = provider or config.LLM_PROVIDER

    if prov == "nvidia":
        result = _call_nvidia(prompt, system)
        if not result.startswith("[NVIDIA API Error:"):
            return result
        # Fallback to ollama
        return _call_ollama(prompt, system)
    elif prov == "ollama":
        return _call_ollama(prompt, system)
    elif prov == "openrouter":
        return _call_openrouter(prompt, system)
    else:
        return f"[Error: Unknown provider '{prov}']"
