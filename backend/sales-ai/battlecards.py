from openai import OpenAI

client = OpenAI()

def generate_battlecard(competitor):

    prompt = f"""
Create a sales battlecard against {competitor}.

Return:

Competitor summary
Weaknesses
How to position against them
One killer question to ask the prospect
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
