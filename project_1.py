import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr
import pyttsx3
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk1  (t):
    engine.say(t)
    engine.runAndWait()

def talke ():
    talk1("Hello , hope you are fine ")
    talk1("Your first name ")
talke ()

def talktime ():
    try:
        print("listening ...")
        with sr.Microphone() as source :
            voice = listener.listen(source)
            Grecog = listener.recognize_google(voice)
            Grecog = Grecog.lower()
            if "john" in Grecog:
                pass
            else :
                talk1("Address my master")
                talk1("Suffer now .......  call me again addressing my master")
                sys.exit()
        return Grecog
    except:
        pass

def talk ():
    try :
        s = talktime ()
        n = s.rindex (" ")
        lt = s[n+1:]
        print (lt)
        if "john" in s :
            s = s.replace("john", "")
            talk1(str(lt) + "tell me what can i do ")
        else :
            pass
    except :
        pass
        sys.exit ()

def run_jarvis ():
    try :
        G = talktime ()
        if "john" in G:
            G=G.replace("john","")
            if  "play" in G or "youtube" in G:
                song =G
                print (song)
                talk1 ("playing from youtube")
                print ("playing...")
                pywhatkit.playonyt(song)
            elif "time" in G :
                time = datetime.datetime.now().strftime('%I: %M  %p')
                talk1("current time is "+time)
                print (time)
            elif "wikipedia" in G or  "information" in G :
                info = wikipedia.summary(G)
                talk1 ("fetching content give me a while ")
                print(info)
                talk1(info)
            elif "google" in G or "search" in G :
                talk1 ("fetching content give me a while ")
                pywhatkit.search(G)
            else :
                talk1("oops i think so , you  provided me insufficient data ")
        else :
            pass
    except :
        sys.exit ()
talk ()
run_jarvis()