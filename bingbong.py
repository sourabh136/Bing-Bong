#Artificical Intelligence
import pyttsx3 
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning Sourabh ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sourabh ")
    else:
        speak("Good Evening Sourabh ")
    
    speak('I am bingbong, How may i help you')

def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Regognizing.....")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return 'None'
    return query
    # pass

def sendEmail(to,content):
    #smtp lib python package
    #search less secure apps in gmail
    #and then enable that function
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    # speak("i am a good boy")
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' or 'open chrome' in query:
            webbrowser.open('google.com')
        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')
        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')
        elif 'open spotify' in query:
            webbrowser.open('spotify.com')
        # elif 'play music' in query:
        #     music_dir="D:\\Non Critical \\songs\\Favouirate Songs2"
            # songs=os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
            #random use kar sakte hai and woh bhi maza aaega
        elif 'the time' in query:
            strTime=datetime.satetime.now().strfTime("%H:%M:%S")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\viren\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(codepath)

        elif 'email to sourabh' in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to = "sourabhshukla836@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send this at this moment")
        
        elif 'quit' in query:
            exit()
        

        #logic for executing task based on query


    # Microsoft Edge
# Version 107.0.1418.62