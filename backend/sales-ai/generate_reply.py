from openai import OpenAI

client = OpenAI()

def generate_reply(text):

    prompt = f"""
You are a senior B2B sales rep.

A prospect sent this message:

{text}

Your task:
- identify the objection
- write a reply that moves the deal forward
- keep it short and natural

Return:

Objection:
Suggested reply:
Goal of reply:
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
