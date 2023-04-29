from dotenv import load_dotenv
import requests

import os

from playsound import playsound

def text_to_speech(text, voice_id="yoZ06aMxZJJ28mfd3POQ"):

    # Load the environment variables from the .env file
    load_dotenv()

    elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

    headers = {
        "Accept": "application/json", 
        "xi-api-key": elevenlabs_api_key
        }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
            }
        }
    
    text_to_speech_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    response = requests.post(text_to_speech_url, json=payload, headers=headers)

    output_file = "./output.mp3"

    if response.ok:
        with open(output_file, 'wb') as f:
            f.write(response.content)

        playsound(output_file)

    else:
        print("Error:", response.status_code)