from backend.slack_agent import app

from backend.sales_ai.generate_reply import generate_reply
from backend.sales_ai.battlecards import generate_battlecard
from backend.sales_ai.analyze_message import analyze_message
from backend.sales_ai.analyze_call import analyze_call

from openai import OpenAI
import json

cliente = OpenAI()

INTENTS_VALIDOS = ["reply", "battlecard", "analyze", "call"]


def classificar_intencao(texto):

    prompt = f"""
Você é um classificador de intenção para um assistente de vendas.

Classifique a mensagem em UMA das intenções abaixo:

reply -> ajudar a escrever uma resposta para um cliente
battlecard -> objeção de concorrente ou posicionamento competitivo
analyze -> analisar mensagem ou conversa de vendas
call -> analisar transcrição de call de vendas

Retorne APENAS JSON válido.

Exemplo:

{{
 "intent": "reply"
}}

Mensagem:
{texto}
"""

    resposta = cliente.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    conteudo = resposta.choices[0].message.content

    print("\n[SAÍDA BRUTA DO CLASSIFICADOR]")
    print(conteudo)

    try:

        dados = json.loads(conteudo)
        intent = dados.get("intent", "analyze")

        if intent not in INTENTS_VALIDOS:
            print("Intent inválido retornado. Usando fallback analyze.")
            intent = "analyze"

        return intent, resposta.usage.total_tokens

    except Exception as erro:

        print("Erro ao interpretar JSON:", erro)
        return "analyze", resposta.usage.total_tokens


@app.event("message")
def tratar_mensagem(body, say):

    evento = body.get("event", {})

    if evento.get("subtype") == "bot_message":
        return

    texto = evento.get("text", "").strip()

    if not texto:
        return

    try:

        intent, tokens_classificador = classificar_intencao(texto)

        print("\n[ROTEADOR DE IA]")
        print("mensagem:", texto)
        print("intent detectado:", intent)
        print("tokens classificador:", tokens_classificador)

        if intent == "reply":

            print("→ enviando para generate_reply")
            resultado = generate_reply(texto)

        elif intent == "battlecard":

            print("→ enviando para battlecards")
            resultado = generate_battlecard(texto)

        elif intent == "call":

            print("→ enviando para analyze_call")
            resultado = analyze_call(texto)

        else:

            print("→ enviando para analyze_message")
            resultado = analyze_message(texto)

        say(resultado)

    except Exception as erro:

        print("Erro no handler:", erro)

        say(
            "Tive um problema ao processar sua mensagem. "
            "Tente novamente ou reformule a pergunta."
        )
