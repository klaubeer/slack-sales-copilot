from openai import OpenAI

client = OpenAI()

def analyze_message(text):

    prompt = f"""
Você é um especialista em vendas B2B SaaS.

Analise a mensagem do cliente abaixo.

MENSAGEM:
{text}

Responda usando esta estrutura:

RISCO DO DEAL
(LOW / MEDIUM / HIGH)

INTENÇÃO PROVÁVEL DO CLIENTE

OBJEÇÕES DETECTADAS

SINAIS DE COMPRA

O QUE O CLIENTE REALMENTE ESTÁ PREOCUPADO

MELHOR PRÓXIMA AÇÃO DO VENDEDOR
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
