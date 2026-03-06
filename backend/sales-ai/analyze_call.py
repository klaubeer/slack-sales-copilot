from openai import OpenAI

client = OpenAI()

def analyze_call(transcript):

    prompt = f"""
Você é um especialista em Revenue Operations.

Analise o trecho de call de vendas abaixo:

{transcript}

Responda em português usando esta estrutura:

ESTÁGIO DO DEAL
(ex: discovery, avaliação, negociação)

OBJEÇÕES DETECTADAS

SINAIS DE COMPRA

RISCOS DO NEGÓCIO

PRÓXIMO PASSO RECOMENDADO

DICA DE COACHING PARA O VENDEDOR
(como melhorar a próxima interação)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
