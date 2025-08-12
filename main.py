#pip install speechrecognition
#pip install setuptools
#pip install pyttsx3
import speech_recognition as sr
import webbrowser
import pyttsx3

import musiclibrary

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def  processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ") [1]  
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    
if __name__ == "__main__":
    speak("hey I am jarvis")
    #listen for wake jarvis
    while True:
        r = sr.Recognizer()
        

        print ("recognizing...")    
        try:
           with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)   
           word = r.recognize_google(audio)
           if(word.lower() == "jarvis"):
               speak("yes")
               with sr.Microphone() as source: 
                    print("Active jarvis...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error;{0}".format(e))

