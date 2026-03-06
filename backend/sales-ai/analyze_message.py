from openai import OpenAI

client = OpenAI()

def analyze_message(text):

    prompt = f"""
Analyze this customer message from a sales perspective.

{text}

Return:

Deal risk (LOW / MEDIUM / HIGH)
Detected objections
Buying signals
Suggested next step
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
