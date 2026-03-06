from backend.slack_agent import app

@app.event("message")
def handle_message(body, say):

    event = body["event"]

    # evita loop com mensagens do próprio bot
    if "bot_id" in event:
        return

    text = event.get("text", "")

    say(f"Recebi: {text}")
