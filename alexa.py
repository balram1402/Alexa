import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talknow(text):
    engine.say(text)  
    engine.runAndWait()

def commandtake():
    try:
        with sr.Microphone() as source:
            print("Listening, Speak up!")   
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
                
    except:
        print("Sorry, there was an issue.")
    return command

def run_alexa():
    command = commandtake()

    if 'play' in command:
        song = command.replace('play','')
        talknow('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talknow('Current time is '+ time)
    elif 'info' in command:
        infor = command.replace('info','')
        details = wikipedia.summary(infor,2)
        print(details)
        talknow(details)
    elif 'joke' in command:
        talknow(pyjokes.get_joke())
    elif 'ache' in command:
        talknow("You need to take tablets and have some sleep!")
    
    else:
        talknow("Sorry, Could you please repeat again!")
    

while True:
    run_alexa()
