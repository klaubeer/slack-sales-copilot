from openai import OpenAI

client = OpenAI()

def analyze_message(text):

    prompt = f"""
Você é um especialista em vendas SaaS B2B.

Analise a mensagem do cliente abaixo.

MENSAGEM:
{text}

A resposta deve ser:
- objetiva
- prática para vendedor
- formato Slack
- máximo ~120 palavras
- usar bullet points

Estrutura:

DEAL RISK
(LOW / MEDIUM / HIGH)

INTENÇÃO DO CLIENTE
(1 frase)

OBJEÇÕES DETECTADAS
• item
• item

SINAIS DE COMPRA
• item
• item

O QUE O CLIENTE REALMENTE ESTÁ PREOCUPADO

MELHOR PRÓXIMA AÇÃO DO VENDEDOR
(ação concreta)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Completion tokens:", response.usage.completion_tokens)
    print("Total tokens:", response.usage.total_tokens)

    return response.choices[0].message.content
