from cgitb import text
from dataclasses import dataclass
from fnmatch import translate
import os
# from bs4 import beautifulsoap, BeautifulSoup
import requests
import WhatsApp
from re import search
import pywhatkit
from time import time
from typing import Text
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from googletrans import Translator
import webbrowser
from playsound import playsound
import pyaudio
import smtplib
from keyboard import press
from keyboard import press_and_release
from keyboard import write

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=12 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
         speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. How may i help you")

    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
   
        return "None"
    return query.lower()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in my Data...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As per my data")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
               webbrowser.open("google.com")

        elif 'open instagram' in query:
               webbrowser.open("instagram.com")      

        elif 'chess online' in query:
               webbrowser.open("Chess.com")

        elif 'open instagram' in query:
            speak("opening Instagram!")
            webbrowser.open("instagram.com")

        elif 'prime music' in query:
            speak("opening Prime music!")
            webbrowser.open("music.amazon.in")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}\n")

        elif 'who created you' in query:
            speak("I was created by my master het.")

        
        elif'what can you do' in query:
            speak("i can do anything as i am an AI and for example, i can tell you the time, play songs, open websites and much more...")


        elif 'open code' in query:
            codePath = "C:\\Users\hetpa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'some favour' in query:
            speak("i'm busy, and i am not able to join your journey.")

        elif 'your specifications' in query:
            speak("i have the speed of processing 4.8 TB per second, core i9 processor, 64 gb of RAM, and supersonic duty of an AI assistant")

        elif 'good job' in query:
            speak("it was my pleasure!")

        elif 'take rest' in query:
        
            speak("thanks sir, you can call me anytime by just telling wake up jarvis.")
            break


        elif 'good night' in query:
            speak("Have a very tasty dream, dont forgot to tell me your dream the next day!")

        elif 'a joke' in query:
            speak("see your face in mirror, a better joke than never!")
            
        elif 'gta V' in query:
            codePath = "C:\\Users\\hetpa\\OneDrive\\Desktop\\Grand Theft Auto V [7L].lnk"
            os.startfile(codePath)

        elif 'watch movie' in query:
            speak("let me show you the latest movies on prime video")
            webbrowser.open("primevideo.com")
        
        elif 'favourite browser' in query:
            speak("here it is!")
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = rememberMsg.replace("jarvis", "")
            speak("you told me to remind you that :+rememberMsg")
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'do you remember' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember" + remember.read())

        elif 'shutdown' in query:
            speak("are you sure?")
            Command = takeCommand()
            if 'yes' in query:
                press_and_release('f4 + alt')

        elif 'how are you' in query:
            speak("i'm always ready to follow your orders, am also not lazy, i'm fit and fine, what about you?")

        elif 'also fine' in query:
            speak("that's a good news for your health, and the extention of my master's life")

        elif 'close tab' in query:
            press_and_release('ctrl + w')

        elif 'new window' in query:
            press_and_release('ctrl + n')

        elif 'chrome history' in query:
            press_and_release('ctrl + h')

        elif 'downloads' in query:
            press_and_release('ctrl + j')

        elif 'bookmarks' in query:
            press_and_release('ctrl + d')

            press('enter')

        elif 'incongnito' in query:
            press_and_release('n + shift + ctrl')

        elif 'switch tabs' in query:
            speak("on which tab you want to jump on, sir?")



        elif 'alarm' in query:
            speak("Tell the time!")
            time = input(": Tell the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Its your time to wakeup.")
                    playsound('the-future-bass-15017.MP321:')
                    speak("Alarm difused!")

                elif now>time:
                    break

        elif 'who' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("who", "")
            query = query.replace("google", "")
            speak("as per google")
            pywhatkit.search(query)

            try:                
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("did't found anything")

def Temp():
     search ="temperature in vadodara" 
     url = "https://www.google.com/search?q={search}"    
     r = requests.get(url)
     data = BeautifulSoup(r.text, "html.parser")
     temperature = data.find("div", class_ = "BNeawe").text
     speak("the temperature out is {temperature} celcius")
def SpeedTest():
            import speedtest
            speak("checking your internet speed")
            speed = speedtest.SpeedTest()
            downloading = speed.download()
            correctDown = int(downloading/800000)
            uploading = speed.upload()
            correctUpload = int(uploading/8000)
            if 'uploading speed' in query:
                speak(f"the uploading speed is{correctUpload} mbps")

            elif 'downloading speed' in query:
                speak(f"the downloading speed is{correctDown} mbps")
                
            else:
                speak(f"the downloading is {correctDown} and the uploading speed is {correctUpload} mbp s ")


