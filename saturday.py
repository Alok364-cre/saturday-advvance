import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import sys 
import pyjokes
import wolframalpha
import requests
import pywikihow


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<24:
        speak("Good Evening!") 

    speak("Loading your AI desktop assistant saturday  hi Boss how can I help you")

def goodwish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening!") 

    elif hour>=21 and hour<24:
        speak("Good Night!") 

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
        print("say that again please....")
        speak("say that again please....")
        return"None"

    return query   

def tellday():
    day=datetime.datetime.today().weekday()+1

    Day_dict ={1:'Monday',2:'Tuesday',
               3:'Wednesday',4:'Thursday',
               5:'Friday',6:'Saturday',
               7:'Sunday'}

    if  day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)    
   
def function():
     wishMe()
     while True:

         query = takeCommand().lower()

         if'wikipedia'in query:
          speak('Searching Wikipedia.....')
          query = query.replace("wikipedia","") 
          results = wikipedia.summary(query,sentences=3)
          speak("According to Wikipedia")
          print(results)
          speak(results)
          speak("sir, do you have any other work")   

         elif 'open youtube'in query:
             speak("Opening")
             webbrowser.open("https://www.youtube.com")
             speak("sir, do you have any other work")   

         elif 'open google'in query:
             speak("Opening")
             webbrowser.open("https://www.google.com")
             speak("sir, do you have any other work")   

         elif 'open instagram'in query:
             speak("Opening")
             webbrowser.open("https://www.instagram.com") 
             speak("sir, do you have any other work")   

         elif 'open facebook'in query:
             speak("Opening")
             webbrowser.open("https://www.facebook.com") 
             speak("sir, do you have any other work")    

         elif 'open stack overflow'in query:
             speak("Opening")
             webbrowser.open("stackoverflow.com")

         elif 'open white'in query or 'open hat' in query:
            speak("Opening")
            webbrowser.open("https://code.whitehatjr.com/s/dashboard") 
            speak("sir, do you have any other work")       
     
         elif'open hotstar' in query:
             speak("opening hotstar")
             webbrowser.open("hotstar.com")
             speak("sir, do you have any other work")  
             
         elif'ip address' in query:
             from requests import get

             ip = get('https://api.ipify.org').text
             speak(F"sir, your unique address is{ip}")
             print(f"sir, your unique address is {ip}") 
             speak("sir, do you have any other work")   

         elif'search' in query:
             speak("searching stuffs")
             query=query.replace('search', '')
             webbrowser.open(query)
             speak("sir, do you have any other work")   
             
         elif'play' in query:
             song = query.replace('play', '')   
             speak("playing")
             pywhatkit.playonyt(song)
             speak("sir, do you have any other work")   

         elif'time' in query:
             strftime = datetime.datetime.now().strftime('%I:%M:%p')
             speak(F"current time is{strftime}")
             print(strftime)
             speak("sir, do you have any other work")   

         elif'which day it is' in query:
             tellday()
             speak("sir, do you have any other work")   
             
         elif'open code' in query:
             speak("opening")
             codePath=("C:\\Users\\Alok Thakur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
             os.startfile(codePath)
             speak("sir, do you have any other work")   

         elif'close code' in query:
             speak("okay sir,closing vscode") 
             os.system("taskkill /f /im code.exe") 
             speak("sir, do you have any other work")        

         elif'open edge' in query:
             speak("opening")
             codePath=("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
             os.startfile(codePath)
             speak("sir, do you have any other work")   

         elif'close edge' in query:
             speak("okay sir,closing Microsoft Edge") 
             os.system("taskkill /f /im msedge.exe")
             speak("sir, do you have any other work")         
  
         elif'open chrome' in query:
             speak("opening")
             codePath=("C:\\Users\\Alok Thakur\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
             os.startfile(codePath)
             speak("sir, do you have any other work")   

         elif'close chrome' in query:
             speak("okay sir,closing chrome") 
             os.system("taskkill /f /im chrome.exe")
             speak("sir, do you have any other work")          

         elif'open pad' in query:
             speak("opening")
             codePath=("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
             os.startfile(codePath)
             speak("sir, do you have any other work")   

         elif'close pad' in query:
             speak("okay sir,closing wordpad") 
             os.system("taskkill /f /im wordpad.exe")        

         elif'open note' in query:
             speak("opening")
             codePath=("C:\\WINDOWS\\system32\\notepad.exe")
             os.startfile(codePath)
             speak("sir, do you have any other work")   

         elif'close note' in query:
             speak("okay sir,closing notepad") 
             os.system("taskkill /f /im notepad.exe")  
             speak("sir, do you have any other work")   
                
         elif'hey Saturday'in query or'ok Saturday'in query:
             speak("yes,boss")
             goodwish()
             tellday()
             speak("sir, do you have any other work")    

         elif'news' in query:
             speak("Here are some headlines from the Times of India,Happy reading")
             news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
             speak("sir, do you have any other work")   

         elif 'who are you' in query or 'what can you do' in query:
            speak('I am saturday version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            speak("sir, do you have any other work")   

         elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by alok")
            print("I was built by alok") 
            speak("sir, do you have any other work") 

         elif 'wait' in query:
            speak("ok sir, I can understand")
            time.sleep(5)

         elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ") 

                speak("sir, do you have any other work")       

         elif'tell me joke' in query:
             speak(pyjokes.get_joke())
             speak("sir, do you have any other work")   

         elif 'ok get some knowledge' in query:
            from pywikihow import search_wikihow
            speak("I can answer to computational and geographical questions  and what question do you want to ask now")
            how=takeCommand().lower() 
            max_results=1
            how_to = search_wikihow( how , max_results)
            assert len(how_to)==1
            how_to[0].print()
            speak(how_to[0].summary)
            speak("sir, do you have any other work") 

         elif 'what is' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            speak("the answer is ")
            answer = next(res.results).text
            speak(answer)
            print(answer)
            speak("sir, do you have any other work")       

         elif "ok quit" in query or 'take some rest' in query or 'ok bye' in query:
                 goodwish()
                 speak("thank you sir,I am going to sleep call me anytime")
                 print("thank you sir,I am going to sleep call me anytime")
                 break 

if __name__ == "__main__":
   function()

            
                 



         
			   





        



    