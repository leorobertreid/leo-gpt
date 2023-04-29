from get_gpt_response import get_gpt_response
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

import speech_recognition as sr

CODE_WORD = "leo"
FILE_TO_WRITE_TO = "Recording.wav"

def main():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                # get code word
                transcription = r.recognize_google(audio)

                if transcription.lower() == CODE_WORD.lower():

                    print("got code word...")

                    with sr.Microphone() as source:
                        r = sr.Recognizer()
                        source.pause_threshold = 1

                        print("listening for the rest...")

                        audio = r.listen(source, phrase_time_limit=None, timeout=None)

                        # write audio found to file
                        with open(FILE_TO_WRITE_TO, "wb") as f:
                            f.write(audio.get_wav_data())

                        # transcribe audio
                        print("transcribing audio...")
                        transcription = speech_to_text()

                        print("getting response from gpt...")
                        output_text = get_gpt_response(transcription)

                        print("saying text...")
                        text_to_speech(output_text)

                        return

            except Exception as e:
                print("an error occured {}".format(e))