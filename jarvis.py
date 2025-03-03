import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import playsound
from googletrans import Translator
import PyPDF2
from bs4 import BeautifulSoup
import pywhatkit
from pywikihow import search_wikihow
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
from pytube import YouTube
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import os
import requests
import datetime
import smtplib
import keyboard
import pyautogui
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate',190)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f": {audio}")
    print("    ")
    Assistant.runAndWait()



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
    
def TaskExe():
    
    Speak("Hello Judges! i am Jarvis your personal AI assistant, how may i help you?")
    
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=5 and hour<12:
            Speak("Good Morning Judges!")
            Speak("Welcome to our project JARVIS.")

        elif hour>=12 and hour<18:
            Speak("Good Afternoon Judges!")
            Speak("I am Jarvis. How may i help you")

        else:
            Speak("Good Evening Judges!")
            Speak("I am Jarvis sir. How may i help you")

    def Music():
        Speak("which song do you want to listen, tell me the name of the song.")
        musicName = Takecommand()

        if 'beat 9 ' in musicName:
            os.startfile('F:\\Users\\hetpa\\Music\\beat 9.mp3')

        else:
            pywhatkit.playonyt(musicName)
            Speak("your song has started playing!, Enjoy sir.")

    def Temp():
                search = "temperature in vadodara"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div",class_ = "BNeawe").text
                Speak(f"The Temperature Outside Is {temperature} ")

                Speak("Do I Have To Tell You Another Place Temperature ?")
                next = Takecommand()

                if 'yes' in next:
                    Speak("Tell Me The Name Of tHE Place ")
                    name = Takecommand()
                    search = f"temperature in {name}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temperature = data.find("div",class_ = "BNeawe").text
                    Speak(f"The Temperature in {name} is {temperature}")

                else:
                    Speak("no problem sir")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = Takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')
            
        elif 'play' in comm:
            keyboard.press('space bar')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm: 
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')
            
        elif 'theatre mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = Takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
            
        elif 'close tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')
            
        elif 'refresh' in query:
            keyboard.press_and_release('F5')

        elif 'private tab' in command:
            keyboard.press_and_release('ctrl + shift + n')

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = Takecommand()

        if 'science chapter 10' in name:

            os.startfile('F:\\jarvis\\Science ch-10.pdf')
            book = open('F:\\jarvis\\Science ch-10.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = Takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')
            else:
                Speak(text)

        elif 'science chapter 13' in name:
            os.startfile('F:\\jarvis\\Science ch-13.pdf')
            book = open('F:\\jarvis\\Science ch-13.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = Takecommand()


        elif 'SS chapter 10' in name:
            os.startfile('F:\\jarvis\\ss chapter 10.pdf')
            book = open('F:\\jarvis\\ss chapter 10.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = Takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)


    def Whatsapp():
        Speak("tell the name of person")
        name = Takecommand()
        if 'shubh' in name:
            Speak("ok, tell me the message")
            msg = Takecommand()
            Speak("tell me the time sir!")
            Speak("tell the hour")
            hour = int(Takecommand())
            Speak("time in minutes")
            min = int(Takecommand())
            pywhatkit.sendwhatmsg(+918000803010,msg,hour,min,20)
            Speak("the message was sent succesfully")

        elif 'meera mam' in name:
            Speak("ok, tell me the message")
            msg = Takecommand()
            Speak("tell me the time sir!")
            Speak("tell the hour")
            hour = int(Takecommand())
            Speak("time in minutes")
            min = int(Takecommand())
            pywhatkit.sendwhatmsg(+917874222250,msg,hour,min,20)

        elif 'bhavya' in name:
            Speak("ok, tell me the message")
            msg = Takecommand()
            Speak("tell me the time sir!")
            Speak("tell the hour")
            hour = int(Takecommand())
            Speak("time in minutes")
            min = int(Takecommand())
            pywhatkit.sendwhatmsg(+917862873035,msg,hour,min,20)

        else:
                Speak("Tell me the number")
                phone = int(Takecommand())
                ph = '+91' + phone
                Speak("ok, tell me the message")
                msg = Takecommand()
                Speak("tell me the time sir!")
                Speak("tell the hour")
                hour = int(Takecommand())
                Speak("time in minutes")
                min = int(Takecommand())
                pywhatkit.sendwhatmsg(phone, msg, hour, min, 20)
            
        Whatsapp()
        
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('shubhhirensoni6906@gmail.com', 'shubh6906_s')
        server.sendmail('shubhhirensoni6906@gmail.com', to, content)
        server.close()
        
        

    while True:

        query = Takecommand()

        if 'hello' in query:
            Speak("Hello sir, i am jarvis your personal AI assistant.")
            Speak("how may i help you?")

        elif 'how are you' in query:
            Speak("I'm fit and fine, what about you?")
            
        elif 'yes' in query:
            Speak("You need a good reason for the ")
            
        elif 'email' in query:
            
            try:
                Speak("What should I say?")
                content = Takecommand()
                to = "hetpatel222008@gmail.com"    
                sendEmail(to, content)
                Speak("Email has been sent!")
            except Exception as e:
                print(e)
                Speak("Sorry my friend. I am not able to send this email")    

        elif 'a break' in query:
            Speak("Ok sir, call me anytime by just saying wakeup jarvis")
            break
        
        elif 'greet' in query:
            wishMe()

        elif 'my school location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@22.3366603,73.2173052,81m/data=!3m1!1e3')

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = Takecommand()
            Speak(f"You Said : {jj}")

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video Downloaded")

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('Clock Alarm.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = Takecommand()
            web = 'https://www.' + name + '.org'
            webbrowser.open(web)
            Speak("Done Sir!")
            
            # For youtube search
       
        elif 'on youtube' in query:            
            Speak("There we go!")
            query = query.replace("jarvis", "")
            query = query.replace("youtube", "")
            query = query.replace("on", "")
            query = query.replace("play", "")
            query = query.replace("hey", "")
            query = query.replace("ok", "")
            query = query.replace("search", "")
            query = query.replace("about", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Request finished!")
            
            # For google search

        elif 'on google' in query:
            Speak("There we go!")
            query = query.replace("jarvis", "")
            query = query.replace("google", "")
            query = query.replace("on", "")
            query = query.replace("search", "")
            query = query.replace("hey", "")
            query = query.replace("ok", "")
            query = query.replace("what", "")
            query = query.replace("about", "")
            query = query.replace("for", "")
            web = 'https://www.google.com/search?q=' + query
            pywhatkit.search(query)
            Speak("Here is what you asked for!")
            
            # For the meaning of any word.
            
        elif 'meaning' in query:
            Speak("There we go!")
            query = query.replace("jarvis", "")
            query = query.replace("google", "")
            query = query.replace("on", "")
            query = query.replace("search", "")
            query = query.replace("hey", "")
            query = query.replace("ok", "")
            query = query.replace("what", "")
            query = query.replace("about", "")
            query = query.replace("for", "")
            web = 'https://www.google.com/search?q=' + query
            pywhatkit.search(query)
            Speak("Here is what you asked for!")
            
            # To open any website

        elif 'website' in query:
            Speak("Ok sir, launching your request")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace("webpage", "")
            query = query.replace("open", "")
            query = query.replace("hey", "")
            query = query.replace("ok", "")
            query = query.replace("of", "")
            query = query.replace(" ", "")
            web1 = query.replace("the", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("request accepted")
            
            # For opening any website or any application.
            
        elif 'open youtube' in query:
            Speak("opening youtube!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'chess online' in query:
            webbrowser.open("Chess.com")
            
        elif 'mail' in query:
            webbrowser.open('gmail.com')

        elif 'open instagram' in query:
            Speak("opening Instagram!")
            webbrowser.open("instagram.com")
            
        elif 'nasa hubblehub' in query:
            Speak("Here is what you asked for!")
            webbrowser.open("hubblehub.org")

        elif 'krunker' in query:
            Speak("opening the game...")
            webbrowser.open("krunker.io")

        elif 'prime music' in query:
            Speak("opening Prime music!")
            webbrowser.open("music.amazon.in")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, The time is {strTime}\n")

        elif 'who created you' in query:
            Speak("I was created by my master.")
            Speak("and, i am a science day project.")

        elif 'what can you do' in query:
            Speak("i can do anything as i am an AI and for example, tell you time, play songs, open websites and much more...")
            
        elif 'about yourself' in query:
            Speak("I am Jarvis. I am an artificial intelligence. I was created in python language and designed in Microsoft Visual Studio Code.")

        elif 'open code' in query:
            Speak("opening vs code")
            codePath = "E:\\ETC\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'zoom' in query:
            os.startfile("C:\\Users\\hetpa\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'py charm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.3\bin\pycharm64.exe")

        elif 'some favour' in query:
            Speak("i'm busy, and i am not able to join your journey.")
            
        elif 'principal mam' in query:
            Speak("Miss Neeta Sanghvi is the principal of bright school.")  
            
        elif 'some favour' in query:
            Speak("i'm busy, and i am not able to join your journey.")

        elif 'song' in query:
            Music()

        elif 'your specifications' in query:
            Speak("i have the speed of processing 4.8 TB per second, core i9 processor, 64 gb of RAM, and supersonic speed of processing.")

        elif 'good job' in query:
            Speak("it was my pleasure!")
            
        elif 'greet the judges' in query:
            Speak("hello! judges, i am jarvis an AI assistant")

        elif 'good night' in query:
            Speak("Have a very tasty dream, dont forgot to tell me your dream the next day!")

        elif 'a joke' in query:
            Speak("see your face in mirror, a better joke than never")

        elif 'gta V' in query:
            codePath = "C:\\Users\\hetpa\\OneDrive\\Desktop\\Grand Theft Auto V [7L].lnk"
            os.startfile(codePath)

        elif 'watch movie' in query:
            Speak("let me show you the latest movies on prime video")
            webbrowser.open("primevideo.com")
            
        elif 'latest movies' in query:
            Speak("let me show you the latest movies on prime video")
            webbrowser.open("primevideo.com")
            
        elif 'am bored' in query:
            Speak("let me show you the latest movies on prime video")
            webbrowser.open("primevideo.com")

        elif 'favourite browser' in query:
            Speak("here it is!")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            Speak("here it is!")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            
            # For accessing wikipedia.

        elif 'wikipedia' in query:
            Speak("Searching on wikipedia...")
            query = query.replace("Jarvis", "")
            query = query.replace("on", "")
            query = query.replace("wikipedia", "")
            query = query.replace("hey", "")
            query = query.replace("ok", "")
            query = query.replace("Tell me about", "")
            query = query.replace("about", "")
            query = query.replace("for", "")
            wiki = wikipedia.summary(query,2)
            Speak(f"according to my source : {wiki}")


        elif 'whatsapp message' in query:
            Whatsapp()
            
            #  For the nasa's space news.
            
        elif 'space news' in query:
            Speak("Tell me the date for the news extraction process...")
            
            Date = Takecommand() 
            
            from Features import DateConverter
            
            value = DateConverter(Date)
            
            from Nasa import NasaNews
            
            NasaNews(value)           
        
            
        elif 'messenger' in query:
            Whatsapp()
            
            # For taking screenschot.
            
        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('E:\\')
            
            #  For greeting anyone.

        elif 'greet' in query:
            wishMe()
            
            # For importing the image from the mars.
            
        elif 'mars image' in query:
            from Nasa import mars_image
            mars_image()
            
        elif 'mass image' in query:
            from Nasa import mars_image
            mars_image()            

        elif 'wish me' in query:
            wishMe()     
            
            # For asking the temperature.
           
        elif 'temperature' in query:
            Temp()
            
            # For automating Youtube.

        elif 'automate youtube' in query:
            YoutubeAuto()
            
            # For automating chrome.

        elif 'automate chrome' in query:
            ChromeAuto()
            
            # For reading a book

        elif 'read a book' in query:
            Reader()
TaskExe()