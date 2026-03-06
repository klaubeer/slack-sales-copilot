from backend.slack_agent import app
from backend.sales_ai.generate_reply import generate_reply
from backend.sales_ai.battlecards import generate_battlecard
from backend.sales_ai.analyze_message import analyze_message


@app.event("message")
def handle_message(body, say):

    event = body.get("event", {})

    # evita loop do próprio bot
    if event.get("subtype") == "bot_message":
        return

    text = event.get("text", "").strip().lower()

    if not text:
        return

    # comando reply
    if text.startswith("reply"):
        query = text.replace("reply", "", 1).strip()
        result = generate_reply(query)
        say(result)
        return

    # comando battlecard
    if text.startswith("battlecard"):
        query = text.replace("battlecard", "", 1).strip()
        result = generate_battlecard(query)
        say(result)
        return

    # comando analyze
    if text.startswith("analyze"):
        query = text.replace("analyze", "", 1).strip()
        result = analyze_message(query)
        say(result)
        return
