from openai import OpenAI

client = OpenAI() 

def analyze_call(transcript):

    prompt = f"""
Você é um Sales Coach especialista em vendas SaaS B2B.

Analise a call abaixo e gere uma análise estratégica do deal.

TRANSCRIÇÃO:
{transcript}

A resposta deve ser:
- clara
- objetiva
- fácil de ler no Slack
- máximo ~200 palavras
- usar bullet points
- evitar parágrafos longos

Estrutura:

DEAL STAGE
(Discovery / Evaluation / Negotiation)

CHAMPION
(quem parece apoiar a solução)

ECONOMIC BUYER
(quem provavelmente controla o orçamento)

DORES PRINCIPAIS
• item
• item

OBJEÇÕES DETECTADAS
• item
• item

SINAIS DE COMPRA
• item
• item

RISCOS DO DEAL
• item
• item

PROBABILIDADE DE FECHAMENTO
(0–100%)

PRÓXIMO PASSO RECOMENDADO
(ação concreta para avançar o deal)

PERGUNTAS QUE O VENDEDOR DEVERIA TER FEITO
• pergunta
• pergunta
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
