import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# plz add your chrome path but don't lost to write %s in the end
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I Am FRIDAY Your Assistant How May I Help You")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if "how are you" in query:
            speak("I am fine and pray for your well being")
            print("I am fine and pray for your well being")
        elif "who are you" in query:
            speak("I am your assistant friday")
            print("I am your assistant friday")
        elif "open twitter" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("twitter.com")
        elif "open youtube" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("youtube.com")
        elif "open whatsapp" in query:
            speak("ok sir, here it is")
            # plz enter your whatsapp path
            codePath = "C:\\Users\\91790\\Desktop\\WhatsApp Desktop"
            os.startfile(codePath)
        elif "open vscode" in query:
            speak("ok sir, here it is")
            # plz enter your V-S-CODE path
            codePath = "C:\\Users\\91790\\Desktop\\Visual Studio Code"
            os.startfile(codePath)
        elif "open chrome" in query:
            speak("ok sir, here it is")
            os.startfile(chrome_path)
        elif "play music" in query:
            speak("ok sir,here it is")
            music_dir = "E:\\music2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)
        elif "thanks friday" in query:
            speak("welcome sir")
            print("welcome sir")
        elif "google search" in query:
            speak("recognizing")
            speak("sir, plz enter what do you want to search")
            pc = input("Enter google search = ")
            speak("searching google...")
            webbrowser.get(chrome_path).open("https://google.com/?q="+pc)
        else:
            print("sorry the command you entered is not satisfied")
            speak("sorry the command you entered is not satisfied")
