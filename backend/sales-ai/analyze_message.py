from openai import OpenAI

client = OpenAI()

def analyze_message(text):

    prompt = f"""
Analise esta mensagem de um cliente em um processo de vendas:

{text}

Responda em português com:

RISCO DO NEGÓCIO
(BAIXO / MÉDIO / ALTO)

OBJEÇÕES DETECTADAS

SINAIS DE COMPRA

PRÓXIMO PASSO SUGERIDO
(o que o vendedor deve fazer agora)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
