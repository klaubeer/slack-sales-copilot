from openai import OpenAI

client = OpenAI()

def generate_battlecard(competitor):

    prompt = f"""
Você é um especialista em inteligência competitiva em SaaS.

Crie um battlecard de vendas contra este concorrente:

CONCORRENTE: {competitor}

Estrutura da resposta:

RESUMO DO CONCORRENTE

PONTOS FORTES

PONTOS FRACOS

EM QUE SITUAÇÕES ELES GANHAM DEALS

COMO POSICIONAR SUA SOLUÇÃO CONTRA ELES

PERGUNTAS QUE O VENDEDOR DEVE FAZER AO CLIENTE

UMA PERGUNTA "KILLER" QUE EXPÕE UMA FRAQUEZA DO CONCORRENTE
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
