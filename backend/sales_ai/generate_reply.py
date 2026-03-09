from openai import OpenAI

client = OpenAI()

def generate_reply(text): 

    prompt = f"""
Você é um vendedor SaaS B2B experiente.

Um prospect enviou a mensagem abaixo.

MENSAGEM:
{text}

Sua tarefa:

1. Identificar a objeção principal
2. Escrever uma resposta curta e natural
3. Avançar o deal

A resposta deve ser:
- curta
- natural
- tom profissional e amigável
- máximo ~80 palavras
- estilo Slack/email

Estrutura:

TIPO DE OBJEÇÃO

RESPOSTA SUGERIDA

OBJETIVO DA RESPOSTA
(o que queremos alcançar com essa resposta)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.4,
        messages=[{"role":"user","content":prompt}]
    )

    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Completion tokens:", response.usage.completion_tokens)
    print("Total tokens:", response.usage.total_tokens)

    return response.choices[0].message.content
