from backend.slack_agent import app
from backend.sales_ai.generate_reply import generate_reply
from backend.sales_ai.battlecards import generate_battlecard
from backend.sales_ai.analyze_message import analyze_message


@app.message("/reply")
def reply_handler(message, say):

    text = message["text"].replace("/reply", "").strip()

    response = generate_reply(text)

    say(response)


@app.message("/battlecard")
def battlecard_handler(message, say):

    competitor = message["text"].replace("/battlecard", "").strip()

    response = generate_battlecard(competitor)

    say(response)


@app.message("/analyze")
def analyze_handler(message, say):

    text = message["text"].replace("/analyze", "").strip()

    response = analyze_message(text)

    say(response)
