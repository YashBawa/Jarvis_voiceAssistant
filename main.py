import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr
import pyttsx3
import pyaudio
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
f=1

def talk1  (t):
    engine.say(t)
    engine.runAndWait()

def talke ():
    engine.say("Hello , hope you are fine ")
    engine.runAndWait()
    engine.say("Your good name ")
    engine.runAndWait()
talke ()

def talktime ():
    try:
        print("listening ...")
        with sr.Microphone() as source :
            # print (source)
            voice = listener.listen(source)
            #print(voice)
            Grecog = listener.recognize_google(voice)
            Grecog = Grecog.lower()
            if "john" in Grecog:
                pass
                #engine.say(Grecog)
                #engine.runAndWait()
                print (Grecog)
            else :
                #engine.say(Grecog)
                print (Grecog)
                engine.say("take my masters name ")
                engine.runAndWait()
                engine.say("Your punishment now , run the program again with masters name")
                engine.runAndWait()
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
            if lt  == "shell":
                talk1("hello, how are you my good friend ")
                talk1("tell what i can do for you")
                return
            else :
                engine.say(str(lt) + "tell what i can do for you")
                engine.runAndWait()
        else :
            pass
    except :
        pass
        sys.exit ()



#a= talktime ()
def run_jarvis ():
    try :
        G=""

        G = talktime ()
        if "john" in G:
            G=G.replace ("john","")
            #print ("g"+G)
            if  "play" in G or "youtube" in G:
                song = G
                print (song)
                talk1 ("playing"+song)
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
                #pywhatkit.
            elif "google" in G and "search" in G :
                talk1 ("fetching content give me a while ")
                pywhatkit.search(G)
        else :
            pass
    except :
        sys.exit ()
talk ()
run_jarvis()