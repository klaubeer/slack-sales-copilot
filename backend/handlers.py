from backend.slack_agent import app
from openai import OpenAI

client = OpenAI()

@app.event("message")
def handle_message(body, say):

    event = body["event"]

    if event.get("subtype") == "bot_message":
        return

    text = event.get("text")

    if not text:
        return

    say("🤖 Pensando...")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful sales copilot."},
            {"role": "user", "content": text}
        ]
    )

    answer = response.choices[0].message.content

    say(answer)
