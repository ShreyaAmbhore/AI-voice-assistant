from pyscreeze import screenshot
import speech_recognition as sr
import pyttsx3
import datetime
import os
import wikipedia
import webbrowser
import smtplib
import psutil
import random
import pyautogui
from bs4 import BeautifulSoup
import webbrowser as wb
import cv2
import numpy as np 
from PIL import Image  
import distutils
camera = cv2.VideoCapture(0)

def jarvis_greet():

    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour <= 17:
        speak("Good afternoon sir")
    elif hour >= 17 and hour < 12:    
        speak("Good evening sir")

    speak("hii there, I am Jarvis. please tell me How may I help you...!")
def screenshot():
    speak('taking screenshot...')
image = pyautogui.screenshot()

        

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RecognizerError as e:
        print(f"Could not get result for : {e}\n")
        return ""
    return query
    
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()
    
def take_photo():
    return_value, image = camera.read()
    if return_value:
        cv2.imwrite("photo.jpg", image)
        speak("Photo Take Successfully")
        
def show_photo():
    image = cv2.imread("photo.jpg",)
    if image is not None:
        cv2.imshow("photo", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        speak("No photo found!")        

if __name__ == '__main__':

    clear = lambda: os.system('cls')

    clear()
    jarvis_greet()

    while True:
        query = listen().lower()
        if "exit" in query:
           exit()
           
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
            
        elif "why you came to this world" in query:
            speak("Further, it is a secret")
                        
        elif query in ('time','current time'):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"Sir, the date is {strDate}")
            
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {query} is {results}")
            
        elif query in ('open youtube','youtube'):
            webbrowser.open("youtube.com")
            
        elif query in ('search google','open google','google'):
            speak("What should i search ?")
            search_term = listen().lower()
            webbrowser.open('https://www.google.com/search?q='+search_term)
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = listen()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
                
        elif 'log out' in query:
            os.system("shutdown -l")
            
        elif 'restart' in query:
            os.system("shutdown  /r /t 1")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
        elif query in ('play songs','music','play music'):
            video ="C:\\Users\\aditi\Videos\Captures"
            audio = 'D:\\New folder'
            speak("What songs should i play? Audio or Video")
            ans = (listen().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (listen().lower())

            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
                    music=random.choice(songs)
                    os.startfile(os.path.join(songs_dir,music))

            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    video = random.choice(songs)
                    print(video)
                    os.startfile(os.path.join(songs_dir,video))
                    
        elif query in ("write a note",'note'):
            speak("What should i write, sir")
            note = listen()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = listen().lower()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)

        elif 'how are you' in query:
            speak("I am fine, buddy Thanks for asking")
            speak("How are you buddy?")
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            else:
                pass
                
        elif query in ('search in chrome','open chrome','chrome'):
            speak("What should I search ?")
            search = listen().lower()
            chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrom',None,webbrowser.BackgroundBrowser(chromepath))
            
            webbrowser.get('chrom').open_new_tab('https://www.google.com//search?q='+search)
            
        elif query in ('word','ms word',' open word'):
            speak("opening MS Word")
            word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk'
            os.startfile(word)
                    
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = listen()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())        
                
        elif query in ('take screenshot','screenshot'):
            screenshot()        
                
        elif query in ('show screenshot',):
            print('Showing Screenshot...')
            speak('Showing Screenshot...')
            image.show()
            image = cv2.cvtColor(np.array(image),
            					cv2.COLOR_RGB2BGR)
            cv2.imwrite("image1.png", image)  
                  
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")        
            
        elif query in ('take photo','take photo','click photo'):
            speak("Taking Photo ")
            print("Taking Photo ")
            take_photo()
        elif query  in ('exit camera','off camera'):
            camera.release()
            cv2.destroyAllWindows()   
            
        elif query in ('show photo','open photo'):
            speak('Showing photo...')
            show_photo()
                          
        else:
            speak("I'm not sure how to respond to that. Please give me commands.")