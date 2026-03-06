from openai import OpenAI

client = OpenAI()

def generate_battlecard(competitor):

    prompt = f"""
Você é um especialista em Revenue Enablement.

Crie um battlecard de vendas contra o concorrente: {competitor}.

Responda em português usando esta estrutura:

RESUMO DO CONCORRENTE
(explicação curta)

QUANDO ELE GANHA NEGÓCIOS
(3 situações comuns)

PONTOS FRACOS
(3-5 fraquezas)

COMO SE POSICIONAR
(como vender contra ele)

FRASE PARA USAR NA CALL
(exemplo de frase que o vendedor pode falar)

PERGUNTA DE DESCOBERTA
(pergunta que expõe a fraqueza do concorrente)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
