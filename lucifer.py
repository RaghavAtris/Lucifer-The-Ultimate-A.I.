# Developer(s) - Raghav Atris and Vayun Yadav
# Project Name - Lucifer The Ultimate A.I.(Desktop Assistant)
# Language Used - Python

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import os
import pywhatkit  # pip install pywhatkit
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import sys
import pyautogui  # pip install pyautogui
import winshell  # pip install winshell
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import cv2  # pip install opencv-python
import webbrowser  
import random
import wikipedia as googleScrap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from luciferUi import Ui_MainWindow
import wolframalpha
try:
    app = wolframalpha.Client("JRTTKA-669QU2HK6A")
except Exception:
    print('Failed to calculate!')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"It's {time}.")
    speak("I'm Lucifer, a virtual artificial intelligence, How can I be of service?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        while True:
            self.TaskExecution()

    def takeCommand(self):

        # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("please repeat...")
            return "None"
        return query

    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'how are you' in self.query:
                speak("I am fine, thank you for asking, what about you?")
                self.query = self.takeCommand().lower()
                if 'fine' in self.query or "good" in self.query or "happy" in self.query or "great" in self.query or "well" in self.query:
                    speak("Good to hear from you!")
                elif 'not fine' in self.query or 'not well' in self.query or 'not good' in self.query or 'sad' in self.query or 'not in mood' in self.query:
                    speak("sad to hear that!")

            elif "wake up" in self.query or "you there" in self.query or "time to work" in self.query or "are you there" in self.query:
                speak(random.choice(["always there for you", "online and ready",
                                     "your wish my command", "at your service"]))

            elif "good morning" in self.query or "good afternoon" in self.query or "good evening" in self.query:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning!")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon!")

                else:
                    speak("Good Evening!")

            elif "hello" in self.query or "hey" in self.query or "hi" in self.query:
                speak(random.choice(["Hello there!",
                      "Hi there!", "Hey there!"]))

            elif "what are you doing" in self.query:
                speak(random.choice(["Well, right now i am learning about quantum computing!", "I'm answering big exisential questions like why fire engines are red",
                      "right now i am talking to you!", "I'm sharing some nutritional facts with my human friends, try asking, lucifer, how much calories are in one apple", "I am helping human communicate with their friends far and wide, Try asking, lucifer, how do you say, hello in french?"]))

            elif 'who made you' in self.query or 'who created you' in self.query or 'who are your developers' in self.query:
                speak(random.choice(['At first i was just an idea, then two creative minds, Raghav Atris and Vayun Yadav came together, And created me!',
                      "I think I first arrived as a burst of inspiration during a good long walk", "Raghav Atris and Vayun Yadav made me, but I'd like to think, i am creative too!"]))

            elif "tell me about yourself" in self.query or "who are you" in self.query or "introduce yourself" in self.query or "describe yourself" in self.query:
                speak(
                    "Now its time to introduce myself. I'm Lucifer, a virtual artificial intelligence, and i am her to assist you to a variety of task since best i can. 24 hours a day, 7 days a week, importing all preferences from home interface, system is now fully operational"
                )

            elif ("what can you do" in self.query or "features" in self.query or "functions" in self.query or "help" in self.query):
                features = ''' I can do a lot of things, and I am learning more, you can ask me to do things like...
                        Tell the current time and date
                        Tell about the weather outside
                        Tell current system status Battery and CPU usage
                        Tell you the top headlines and latest news
                        Tell the location of any place in the world
                        Calculate any mathematical expressions
                        Launch applications, softwares and websites
                        Search your queries via Wikipedia and Google
                        Play your favourite songs on YouTube
                        Voice, Music and Media Control, Pause, Play, Stop, increase voulume, decrease volume
                        Window Control Minimize, Maximize, Switch Applications
                        Shut down, restart and hibernate your system
                        It can also help you pick up where you left off. Try saying, Lucifer, Show my recent files
                        It has a search engine made by my developers, if you want to know something just say the query, and it will give you the answer
                        So, how can i help you?
                        '''
                speak(features)
            
            elif "location" in self.query or "where am I" in self.query:
                speak("please wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(
                        f"I am not sure, but i think you are currently in {city} city of {country} country")
                except Exception as e:
                    speak(
                        "sorry, due to network issue, i am not able to find where we are. Please try again")
                    pass

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takeCommand().lower()
                timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')
                
                import time
                time.sleep(timing)
                speak('Your time has been finished!')

            elif 'play' in self.query:
                song = self.query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)

            elif "joke" in self.query:
                speak(pyjokes.get_joke())
                print(pyjokes.get_joke())

            elif "news" in self.query or 'headlines' in self.query or "buzzing" in self.query:
                speak("please wait, fetching the latest news")
                main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=506bf612a20742b881438715a5a5173f'
                main_page = requests.get(main_url).json()
                articles = main_page["articles"]
                head = []
                day = ["first", "second", "third", "fourth", "fifth"]
                for ar in articles:
                    head.append(ar["title"])
                for i in range(len(day)):
                    speak(f"{head[i]}")

            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f"It's {time}.")

            elif 'date' in self.query:
                date = datetime.datetime.now().strftime("%b %d %Y")
                speak(f"It's {date}")

            elif 'weather' in self.query:
                search = "weather"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                weather = data.find("div", class_="BNeawe").text
                speak(f"The weather outside is {weather}")

            elif 'calculate' in self.query:
                app_id = "JRTTKA-669QU2HK6A"
                client = wolframalpha.Client(app_id)
                indx = self.query.lower().split().index('calculate')
                self.query = self.query.split()[indx + 1:]
                res = client.query(' '.join(self.query))
                answer = next(res.results).text
                speak("The answer is " + answer)
                print("The answer is " + answer)

            elif "ip address" in self.query:
                ip = requests.get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"our system have {percentage} percent battery")
                if percentage >= 50:
                    speak("we have enough power to continue our work")
                elif percentage >= 30 and percentage <= 50:
                    speak(
                        "we should connect our system to charging point to continue our work")
                elif percentage >= 15 and percentage <= 30:
                    speak(
                        "we don't have enough power to continue our work, we should connect our system to charging point to continue our work ")
                elif percentage <= 15:
                    speak(
                        "we are draining, please connect our system to charging point or our system will shutdown soon")

            elif "open camera" in self.query:
                speak(random.choice(
                    ["Sure!, opening camera", "Alright!, opening camera"]))
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'type' in self.query:
                self.query = self.query.replace("type", "")
                pyautogui.write(self.query)

            elif 'cpu' in self.query:
                usage = str(psutil.cpu_percent())
                speak("CPU is at" + usage + "Percent")

            elif "increase" in self.query or "turn up" in self.query:
                pyautogui.press("volumeup")
                speak("I've turned it up.")

            elif "decrease" in self.query or "turn down" in self.query:
                pyautogui.press("volumedown")
                speak("I've turned it down")

            elif 'switch' in self.query or 'change' in self.query:
                speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif 'minimise' in self.query:
                speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("win")
                pyautogui.press("down")
                pyautogui.keyUp("win")

            elif "maximize" in self.query:
                speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")

            elif 'close' in self.query:
                speak(random.choice(
                    ["closing...", "terminating..."]))
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                pyautogui.keyUp("alt")

            elif "open" in self.query or "launch" in self.query:
                try:
                    self.query = self.query.replace("open", "")
                    speak(random.choice(
                        ["opening..."+self.query, "Lauching..."+self.query]))
                    pyautogui.press('win')
                    pyautogui.write(self.query)
                    pyautogui.press('\n')
                except:
                    speak("It doesn't look like you have an app like that")

            elif "note" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
                speak("What would you like me to note down?")
                self.query = self.takeCommand().lower()
                pyautogui.write(self.query)
                speak("I've made a note of that")

            elif 'lock' in self.query:
                import ctypes
                try:
                    speak("locking your device")
                    ctypes.windll.user32.LockWorkStation()
                except Exception as e:
                    speak("window is already locked")

            elif 'empty recycle bin' in self.query:
                try:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Alright, cleaning recycle bin")
                    import time
                    time.sleep(3)
                    speak("Recycle Bin is cleaned")
                except Exception as e:
                    speak("Recycle bin is already cleaned")

            elif 'username' in self.query or 'user' in self.query or 'user name' in self.query or "name" in self.query:
                username = psutil.users()
                for user_name in username:
                    first_name = user_name[0]
                    speak(
                        f"This computer is signed to {first_name} as a username.")

            elif "shutdown" in self.query:
                speak("okay, please wait, Initializing shutdown protocol")
                os.system("shutdown /s /t 5")

            elif "restart" in self.query:
                speak("okay, please wait, restarting your computer")
                os.system("shutdown /r /t 5")

            elif "hibernate" in self.query:
                speak("okay, please wait, hibernating your computer")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "thank you" in self.query:
                speak(random.choice(
                    ["your most welcome!", "No probelem!", "My pleasure!"]))

            elif "what" in self.query or "which" in self.query or "who" in self.query or "when" in self.query or "how" in self.query or "why" in self.query or "tell me" in self.query:
                self.query = self.query.replace("lucifer", "")
                self.query = self.query.replace("tell me", "")
                speak("This is what i fonud on the web")

                try:
                    pywhatkit.search(self.query)
                    result = googleScrap.summary(self.query, 2)
                    speak(result)

                except:
                    speak("no speakable data available for this query")

            elif "where" in self.query:
                self.query = self.query.replace("where", "")
                self.query = self.query.replace("is", "")
                self.query = self.query.replace("city", "")
                self.query = self.query.replace("state", "")
                self.query = self.query.replace("country", "")
                self.query = self.query.replace("located", "")
                self.query = self.query.replace("location", "")
                url = 'https://google.nl/maps/place/' + self.query + '/&amp;'

                webbrowser.open(url)
                speak(f'location of {self.query} is on your screen')

            elif "good night" in self.query:
                speak("ALright, going offline, Goodnight, Sweet dreams!")
                sys.exit()

            elif "goodbye" in self.query or "bye" in self.query or "good bye" in self.query or "offline" in self.query or "break" in self.query or "sleep" in self.query:
                speak("nice talking to you!")
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    speak("Have a Nice day!")
                    sys.exit()
                elif hour >= 18 and hour < 24:
                    speak("Goodnight, Sweet dreams!")
                    sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "lucifer_gif.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
lucifer = Main()
lucifer.show()
sys.exit(app.exec_())