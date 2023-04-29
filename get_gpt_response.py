import openai

from dotenv import load_dotenv
import os

import json

def get_gpt_response(input_text):

    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key

    message_data = []

    with open("data/system-message.json", "r") as f:
        message_data.append(json.load(f))

    with open("data/chat-history.json", "r") as f:
        chat_history = json.load(f)

        for i in chat_history:
            message_data.append(i)

    message_data.append({"role": "user", "content": input_text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_data
    )

    response_text = response.choices[0].message.content

    message_data.append({"role": "assistant", "content": response_text})

    message_data.pop(0)

    with open("data/chat-history.json", "w") as f:
        json.dump(message_data, f)

    return(response_text)