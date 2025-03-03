import os
import speech_recognition as sr

def Takecommand():
    Command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        Command.pause_threshold = 1
        audio = Command.listen(source)


        try:
            print("Recognising...")
            query = Command.recognize_google(audio,language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            print(Error)
            return "none"

        return query.lower()
    
while True:
    wake_up = Takecommand()
    
    if 'wake up' in wake_up:
        os.startfile('D://jarvis//jarvis.py')
        
    else:
        print("Nothing found...")