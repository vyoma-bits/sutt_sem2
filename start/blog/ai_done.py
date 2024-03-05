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
        "X-RapidAPI-Key": "23ffcdd161msh2f900f53717411ap1b95b2jsn7386a33d5477",
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Convert the response content to a string
    response_text = response.text
    return response_text


