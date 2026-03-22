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

PONTOS FORTES

PONTOS FRACOS

QUANDO ELES GANHAM

COMO POSICIONAR CONTRA

PERGUNTAS PARA O CLIENTE

PERGUNTA KILLER
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    print("Tokens usados:", response.usage.total_tokens)

    return response.choices[0].message.content
