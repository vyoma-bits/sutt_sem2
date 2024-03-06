import requests

def ai(content):
    url = "https://open-ai21.p.rapidapi.com/conversationmpt"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": str(content)
            }
        ],
        "web_access": False
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "453a758bf1msh21cbadc89f9dd6bp103bb4jsn0f94ca2a8dbc",
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Convert the response content to a string
    response_text = response.text
    return response.json


