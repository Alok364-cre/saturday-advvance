import speech_recognition as sr
import os


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold=5000
        r.pause_threshold=0.8
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query =r.recognize_google(audio, language='en-in')
        print(F"user said: {query}\n")    
        
    except Exception as e:
        print("bas mein har chiz nahi dhonda shakti")
        speak("bas mein har chiz nahi dhoonda shakti")
        return"None"

    return query   

while True:
    wake_up = takeCommand()

    if 'wake up saturday' in wake_up:
        os.startfile("C:\\Users\\Alok Thakur\\Downloads\\saturday.py")
    else:
        print("nothing......")


