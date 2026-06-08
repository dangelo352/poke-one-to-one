from fastapi import FastAPI, Request
from agent import Agent
import uvicorn

app = FastAPI()
agent = Agent()

@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.json()
    
    # Example logic for generic webhooks (e.g., Twilio, Typeform)
    # You would parse the specific format here
    print(f"Received webhook: {payload}")
    
    # If the payload has a 'text' field, we can process it
    message = payload.get("text") or payload.get("body")
    if message:
        response = agent.run(message)
        return {"status": "success", "response": response}
    
    return {"status": "ignored", "reason": "No message content found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
