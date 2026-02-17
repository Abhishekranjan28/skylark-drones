import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": os.getenv("MONDAY_API_TOKEN"),
    "Content-Type": "application/json"
}


def fetch_board(board_id):

    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            id
            name
            column_values {{
              id
              text
              type
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(URL, json={"query": query}, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Monday API Error")

    return response.json()["data"]["boards"][0]["items_page"]["items"]
