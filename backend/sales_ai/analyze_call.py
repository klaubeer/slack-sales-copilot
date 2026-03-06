from openai import OpenAI

client = OpenAI()

def analyze_call(transcript):

    prompt = f"""
Você é um Sales Coach especialista em vendas SaaS B2B.

Analise a call de vendas abaixo.

TRANSCRIÇÃO:
{transcript}

Produza uma análise estratégica do deal usando esta estrutura:

ESTÁGIO DO DEAL
(ex: discovery, qualificação, avaliação, negociação)

CHAMPION IDENTIFICADO
(quem parece defender a solução internamente)

POSSÍVEL ECONOMIC BUYER
(quem provavelmente controla o orçamento)

PRINCIPAIS DORES DO CLIENTE

OBJEÇÕES DETECTADAS

SINAIS DE COMPRA

RISCOS DO DEAL

PROBABILIDADE DE FECHAMENTO
(0–100%)

PRÓXIMA AÇÃO RECOMENDADA
(o que o vendedor deve fazer para avançar o deal)

PERGUNTAS QUE O VENDEDOR DEVERIA TER FEITO
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
