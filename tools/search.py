import requests
from config import Config

def web_search(query: str):
    """
    Performs a web search using the Tavily API.
    """
    if not Config.TAVILY_API_KEY:
        return "Tavily API key not configured."
        
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": Config.TAVILY_API_KEY,
        "query": query,
        "search_depth": "smart"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Search failed: {str(e)}"
