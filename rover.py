import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb

rover=pyttsx3.init()
voice=rover.getProperty('voices')
rover.setProperty('voice',voice[1].id)

def speak(audio):
    print('R.O.V.E.R.: ' + audio)
    rover.say(audio)
    rover.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I: %M : %p")    
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Ohayo")
    elif hour >=12 and hour<18:
        speak("Konnichiwa")
    elif hour >=18 and hour<24:
        speak("Konbanwaa")
    speak(' How can i help you')
        
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Son sama :" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query=str(input('Your order is: '))
    return query
            
if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search Goshujinsama?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Rover is quitting Goshujinsamaa  Saayonaraa")
            quit()

            


