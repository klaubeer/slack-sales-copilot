from slack_agent import app

@app.message("hello")
def say_hello(message, say):
    say("Hello 👋")
