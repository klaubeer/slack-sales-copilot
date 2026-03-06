from openai import OpenAI

client = OpenAI()

def analyze_message(text):

    prompt = f"""
You are a B2B SaaS sales strategist.

Analyze the following prospect message.

MESSAGE:
{text}

Return the analysis in this structure:

DEAL RISK
(LOW / MEDIUM / HIGH)

LIKELY INTENT OF THE PROSPECT

DETECTED OBJECTIONS

BUYING SIGNALS

WHAT THE PROSPECT IS REALLY WORRIED ABOUT

BEST NEXT ACTION FOR THE SALES REP
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
