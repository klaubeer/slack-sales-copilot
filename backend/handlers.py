from backend.slack_agent import app

from backend.sales_ai.generate_reply import generate_reply
from backend.sales_ai.battlecards import generate_battlecard
from backend.sales_ai.analyze_message import analyze_message
from backend.sales_ai.analyze_call import analyze_call

from openai import OpenAI
import json

client = OpenAI()


def route_intent(text):
    """
    Classifica a intenção da mensagem usando LLM.
    Retorna uma das intenções:
    reply | battlecard | analyze | call
    """

    prompt = f"""
Você é um classificador de intenções para um assistente de vendas.

Classifique a mensagem abaixo em uma das intenções:

reply → quando o vendedor quer ajuda para responder um cliente
battlecard → quando quer ajuda para competir contra um concorrente
analyze → quando quer analisar uma mensagem de cliente
call → quando envia um trecho de call de vendas

Mensagem:
{text}

Responda em JSON neste formato:

{{
 "intent": "reply | battlecard | analyze | call"
}}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        parsed = json.loads(content)
        return parsed.get("intent", "analyze")
    except:
        return "analyze"


@app.event("message")
def handle_message(body, say):

    event = body.get("event", {})

    # evita loop com mensagens do próprio bot
    if event.get("subtype") == "bot_message":
        return

    text = event.get("text", "").strip()

    if not text:
        return

    try:

        intent = route_intent(text)

        if intent == "reply":
            result = generate_reply(text)

        elif intent == "battlecard":
            result = generate_battlecard(text)

        elif intent == "call":
            result = analyze_call(text)

        else:
            result = analyze_message(text)

        say(result)

    except Exception as e:

        print("Erro no handler:", e)

        say(
            "Tive um problema ao processar sua mensagem. "
            "Tente novamente ou reformule a pergunta."
        )
