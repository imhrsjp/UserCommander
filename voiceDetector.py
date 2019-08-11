import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def spoke():
    speak("I am hydra H, here i am to solve your problem.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Harsh")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Harsh")

    elif hour>=18 and hour<22:
        speak("Good evening harsh")

    else:
        speak("Good night Harsh")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What can i do for you sir?")
        speak("What can i do for you sir?")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio,language='en-in')
        print("User said: ",query)

    except:
        print("Speak again please")
        return "none"

    return query

def yes():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        qqry = r.recognize_google(audio,language='en-in')

    except:
        print("Speak again please")
        return "none"

    return qqry


def jump():
    print("Order please")
    
    qry = take_command().lower()
    if 'open google' in qry:
        webbrowser.open("google.com")

    elif 'open youtube' in qry:
        webbrowser.open("youtube.com")

    elif 'open stackoverflow' in qry:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in qry:
        music_dir = "C:\\harsh\\music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'open code' in qry:
        codepath = "C:\\Users\\HARSH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'wikipedia' in qry:
        speak("Searching sir")
        query = qry.replace("wikipedia","")
        results = wikipedia.summary(query,"sentences=2")
        print(results)
        speak(results)

    elif 'time' in qry:
        stime = datetime.datetime.now().strftime("%H:%M:%S")
        print(stime)
        speak(f"sir, The time is {stime}")

    elif 'date' in qry:
        sdate = datetime.datetime.now().strftime("%D")
        print(sdate)
        speak(sdate)

    
        

def main():
    wishme()
    spoke()
    jump()

main()
