import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_summary(query, metrics, caveat):

    prompt = f"""
You are advising a founder.

Question:
{query}

Metrics:
{metrics}

Data Quality:
{caveat}

Provide:
- Executive summary
- Insights
- Risks
- Recommendations

Do not invent numbers.
"""

    return model.generate_content(prompt).text
