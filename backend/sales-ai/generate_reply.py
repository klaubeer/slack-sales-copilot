from openai import OpenAI

client = OpenAI()

def generate_reply(text):

    prompt = f"""
Você é um vendedor B2B experiente.

Um lead enviou esta mensagem:

{text}

Analise a mensagem e responda em português com:

OBJEÇÃO IDENTIFICADA
(resuma o problema do cliente)

RESPOSTA SUGERIDA
(mensagem curta e natural que avance o negócio)

OBJETIVO DA RESPOSTA
(ex: marcar reunião, avançar para demo, etc)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
