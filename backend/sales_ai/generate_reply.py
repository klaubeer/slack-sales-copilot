from openai import OpenAI

client = OpenAI()

def generate_reply(text):

    prompt = f"""
Você é um vendedor SaaS B2B com mais de 10 anos de experiência.

Um prospect enviou a seguinte mensagem:

{text}

Sua tarefa:

1. Identificar a objeção principal
2. Escrever uma resposta curta e natural que avance o deal
3. Manter tom profissional e amigável

Estrutura da resposta:

TIPO DE OBJEÇÃO

RESPOSTA SUGERIDA

OBJETIVO DA RESPOSTA
(o que essa resposta tenta alcançar no processo de venda)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
