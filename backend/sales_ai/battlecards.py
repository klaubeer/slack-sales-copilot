from openai import OpenAI

client = OpenAI()

def generate_battlecard(competitor):

    prompt = f"""
Você é um especialista em inteligência competitiva em SaaS B2B.

Crie um battlecard de vendas contra o concorrente abaixo.

CONCORRENTE: {competitor}

A resposta deve ser:
- curta
- prática para uso por vendedores
- otimizada para leitura no Slack
- usar bullet points
- evitar parágrafos longos
- máximo ~150 palavras

Estrutura obrigatória:

BATTLECARD — {competitor}

RESUMO
(1–2 frases)

PONTOS FORTES
• item
• item
• item

PONTOS FRACOS
• item
• item
• item

QUANDO ELES GANHAM
• situação
• situação

COMO POSICIONAR CONTRA
• argumento de venda
• argumento de venda

PERGUNTAS PARA O CLIENTE
• pergunta
• pergunta

PERGUNTA KILLER
(uma pergunta curta que exponha fraqueza do concorrente)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
