import os
import speech_recognition as sr


def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        print("          ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

while True:

    wake_Up = takecommand

    if 'wake up' in wake_Up:
        os.startfile('C:\\Users\\BRIGHT SCHOOL\\jarvis\\jarvis.py')

    else:
        print("Nothing found....!")