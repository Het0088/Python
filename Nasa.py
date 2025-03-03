import requests
import os
from PIL import Image
import pyttsx4

Assistant = pyttsx4.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate',190)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f": {audio}")
    print("    ")
    Assistant.runAndWait()


api_key = 't4O7Q1lWgqJIhpXfB17eHn4bMVrri3qurfsyCLLM'

def NasaNews(Date):

    Speak("Extracting Data From Nasa server. ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(api_key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    fileName = str(Date) + '.jpg'

    with open(fileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "F:\\jarvis\\" + str(fileName)
    
    Path_2 = "F:\\jarvis\\Nasa\\" + str(fileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")
    
# NasaNews('')
    
def mars_image():
    name = 'curiosity'
    
    dateI = '2021-02-18'
    
    Api_ = str(api_key)
    
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={dateI}&api_key={Api_}"
    
    print(url)
    
    r = requests.get(url)
    
    data = r.json()
    
    photos = data['photos'][:4]
    
    try:
        
        for index , photo in enumerate(photos):
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_pf_photo = photo['earth_date']
            img_url = photo['img_src']
            p = requests.get(img_url)
            img = f'{index}.jpg'
            with open(img,'wb') as file:
                file.write(p.content)
                
            path_1 = "F:\\jarvis\\" + str(img)
            path_2 = "F:\\jarvis\\Nasa\\MARS IMAGE\\" + str(img)
            
            os.replace(path_1,path_2)
            
            os.startfile(path_2)
            
            Speak(f"This image was captured with : {full_camera_name} on {date_pf_photo} with the rover{rover_name}")
            
            
    except:
        Speak("nothing found...")
        
# mars_image()