import speech_recognition as sr

def speech_to_text(audio_path="Recording.wav"):
    r = sr.Recognizer()
    # open the audio file using the recognizer
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)  # read the entire audio file
    
    # convert speech to text
    text = r.recognize_google(audio_data)

    # print the text
    return text