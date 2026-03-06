from openai import OpenAI

client = OpenAI()

def analyze_call(transcript):

    prompt = f"""
Você é um Sales Coach AI especialista em vendas SaaS B2B.

Analise a call de vendas abaixo e produza uma análise estratégica do deal.

TRANSCRIPT:
{transcript}

Responda em português usando EXATAMENTE esta estrutura:

DEAL STAGE
(ex: discovery, qualification, evaluation, negotiation)

CHAMPION IDENTIFICADO
(quem parece apoiar a solução)

ECONOMIC BUYER
(quem provavelmente controla o orçamento)

PRINCIPAIS DORES DO CLIENTE

OBJEÇÕES DETECTADAS

SINAIS DE COMPRA

RISCOS DO DEAL

PROBABILIDADE DE FECHAMENTO
(0–100%)

PRÓXIMA AÇÃO RECOMENDADA
(ação específica para avançar o deal)

PERGUNTAS QUE O VENDEDOR DEVERIA TER FEITO
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
