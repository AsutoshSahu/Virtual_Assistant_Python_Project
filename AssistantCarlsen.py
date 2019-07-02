import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
#getting the available voices in the system
voices = engine.getProperty('voices')
#setting the male voice as assistant i.e. index[0], index[1] for female voice
engine.setProperty('voice', voices[0].id)

'''this func enables our assistant to speak the text passed as parameter'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''this func makes assistant wish the user according to the time'''
def wishMe():
    '''hour is converted into int and then checked'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Carlsen Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #waits for one second whenever the user takes a pause and after this duration if user doesn't speak then assistant considers it to be the query
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pintracano@gmail.com', 'Saraimu$')
    server.sendmail('pintracano@gmail.com', to, content)
    server.close()

#similar to the main func in c(default func)
if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")   

        elif 'play music' in query:
            #double backslash needs to be given other compiler considers it to be escape character
            music_dir = 'D:\\extra\\Music PC'
            songs = os.listdir(music_dir)  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open movies' in query:
            moviesPath = "D:\\extra\\VIDEOS\\MOVIES"
            os.startfile(moviesPath)

        elif 'open snake game' in query:
            gamePath = "C:\\Program Files\\SNAKE GAME BY ASUTOSH\\SNAKEGAME.exe"
            os.startfile(gamePath)

        elif 'open turtle race game' in query:
            gamePath1 = "E:\\software\\Python 3.7\\TURTLE RACE\\TURTLE RACE.py"
            os.startfile(gamePath1)

        elif 'open A S paint' in query:
            paintPath = "E:\\software\\Python 3.7\\AS PAINT\\ASpaint.py"
            os.startfile(paintPath)

        elif 'open photoshop' in query:
            psPath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2018\\Photoshop.exe"
            os.startfile(psPath)

        elif 'open illustrator' in query:
            ilPath = "C:\\Program Files\\Adobe\\Adobe Illustrator CC 2017\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(ilPath)

        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'open camera' in query:
            camPath = "%SystemRoot%\\Camera\\Camera.exe"
            os.startfile(camPath)

        elif 'open poer point' in query:
            ppPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppPath)

        elif 'open share it' in query:
            siPath = "C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
            os.startfile(siPath)

        elif 'email to Anisha' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "2ndjananu@gmail.com"    
                sendEmail(to, content)
                speak("Mail has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am unable to send the mail at the moment")    

