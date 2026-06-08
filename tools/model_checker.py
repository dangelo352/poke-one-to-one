import time
import requests
from config import Config

class ModelChecker:
    """
    Diagnostic tool to verify connectivity and latency for configured AI providers.
    """
    def __init__(self, user_keys=None):
        self.keys = user_keys or {}
        # Merge config keys if not provided in user_keys
        self.config_map = {
            "openai": self.keys.get("openai_api_key") or Config.OPENAI_API_KEY,
            "anthropic": self.keys.get("anthropic_api_key") or Config.ANTHROPIC_API_KEY,
            "gemini": self.keys.get("gemini_api_key") or Config.GEMINI_API_KEY,
            "xai": self.keys.get("xai_api_key") or Config.XAI_API_KEY,
        }

    def check_openai(self):
        key = self.config_map["openai"]
        if not key: return {"status": "Missing Key", "latency": None}
        
        start = time.time()
        try:
            resp = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "model": Config.DEFAULT_MODEL,
                    "messages": [{"role": "user", "content": "ping"}],
                    "max_tokens": 1
                },
                timeout=10
            )
            latency = round(time.time() - start, 2)
            if resp.status_code == 200:
                return {"status": "Live", "latency": f"{latency}s"}
            return {"status": f"Error {resp.status_code}", "latency": f"{latency}s"}
        except Exception as e:
            return {"status": f"Failed: {str(e)[:30]}", "latency": None}

    def check_xai(self):
        key = self.config_map["xai"]
        if not key: return {"status": "Missing Key", "latency": None}
        
        start = time.time()
        try:
            resp = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "model": Config.GROK_MODEL,
                    "messages": [{"role": "user", "content": "ping"}],
                    "max_tokens": 1
                },
                timeout=10
            )
            latency = round(time.time() - start, 2)
            if resp.status_code == 200:
                return {"status": "Live", "latency": f"{latency}s"}
            return {"status": f"Error {resp.status_code}", "latency": f"{latency}s"}
        except Exception as e:
            return {"status": f"Failed: {str(e)[:30]}", "latency": None}

    def run_diagnostics(self):
        print("\n" + "="*40)
        print("     POKE MODEL CONNECTIVITY REPORT")
        print("="*40)
        
        results = {
            "OpenAI": self.check_openai(),
            "xAI (Grok)": self.check_xai(),
            "Anthropic": {"status": "Implementation Pending", "latency": None},
            "Gemini": {"status": "Implementation Pending", "latency": None}
        }
        
        for provider, info in results.items():
            status_str = f"[{info['status']}]"
            latency_str = f"({info['latency']})" if info['latency'] else ""
            print(f"{provider:<15} {status_str:<25} {latency_str}")
        
        print("="*40 + "\n")
        return results
