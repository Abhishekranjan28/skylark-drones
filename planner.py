import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

PROMPT = """
You are a BI query planner.

Return JSON only:

{
  "board": "deals | work_orders | both",
  "analysis": "pipeline | revenue | execution | leadership",
  "filters": {
      "sector": "string or null",
      "time_period": "current_quarter | current_month | null"
  }
}
"""


def generate_plan(query):

    response = model.generate_content(PROMPT + "\nUser Question:\n" + query)

    try:
        text = response.text
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except:
        return None
