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

    def check_anthropic(self):
        key = self.config_map["anthropic"]
        if not key: return {"status": "Missing Key", "latency": None}
        
        start = time.time()
        try:
            resp = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                },
                json={
                    "model": "claude-3-5-sonnet-20240620",
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

    def check_gemini(self):
        key = self.config_map["gemini"]
        if not key: return {"status": "Missing Key", "latency": None}
        
        start = time.time()
        try:
            # Using Google AI Studio (Gemini API) format
            resp = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}",
                headers={"Content-Type": "application/json"},
                json={
                    "contents": [{"parts": [{"text": "ping"}]}],
                    "generationConfig": {"maxOutputTokens": 1}
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
            "Anthropic": self.check_anthropic(),
            "Gemini": self.check_gemini(),
            "xAI (Grok)": self.check_xai()
        }
        
        for provider, info in results.items():
            status_str = f"[{info['status']}]"
            latency_str = f"({info['latency']})" if info['latency'] else ""
            print(f"{provider:<15} {status_str:<25} {latency_str}")
        
        print("="*40 + "\n")
        return results

    def run_routing_test(self, router):
        """
        Simulates routing decisions based on various prompts.
        """
        test_cases = [
            {"name": "Simple Greeting", "prompt": "Hi there, how's it going?"},
            {"name": "Complex Coding", "prompt": "Refactor this python script to use async/await for network requests."},
            {"name": "Deep Analysis", "prompt": "Analyze the architectural differences between event-driven and monolithic systems."},
            {"name": "Grok Specific", "prompt": "Hey Grok, what's the latest trend in AI?"},
            {"name": "Large Context", "prompt": "Summarize this data...", "tokens": 5000}
        ]
        
        print("="*60)
        print(f"{'TEST CASE':<20} | {'MODEL SELECTED':<25} | {'PROVIDER'}")
        print("-" * 60)
        
        for case in test_cases:
            tokens = case.get("tokens", 0)
            model, provider = router.get_model(case["prompt"], token_estimate=tokens)
            print(f"{case['name']:<20} | {model:<25} | {provider}")
        
        print("="*60 + "\n")
