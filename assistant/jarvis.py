import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import pywhatkit
from datetime import date
import calendar
import time
import email
import traceback
import imaplib
import operator
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('i am heyley,your virtual assistant. how may i help you?')


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=0.8
        r.energy_threshold=600
        audio=r.listen(source)

    try:
        print('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)

        print('say that again please...')
        return 'none'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('smitaspn08@gmail.com','spn08smita')
    server.sendmail('smita1997spn@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak (results)
        elif 'open youtube' in query:
            speak('what should i search')
            content=takeCommand()
            
            pywhatkit.playonyt(content)
            speak('playing video')

        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')  
            
        elif 'introduce yourself' in query:
            intro='Hii, this is heyley. developed by smita srivastava,student of doctor shakuntala misra university,lucknow'
            print(intro)
            speak(intro)
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')
        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open('web.whatsapp.com')
        elif 'play music in you tube' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%I:%M %p')
            speak(f"mam, the time is{strtime}")
        elif 'current date' in query:
            today=date.today()
            print(today)          
            speak(f"mam the date is{today}")
        elif 'the day' in query:
            curr_date=date.today()
            day=(calendar.day_name[curr_date.weekday()])
            print(f"mam, today is {day}")
            speak(f"mam, today is {day}")
            
        
        elif 'open vs code' in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening vs code')
            os.startfile(codepath)
        elif 'vlc player' in query:
            vlcpath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            speak('opening vlc media player')
            os.startfile(vlcpath)
        elif 'play song' in query:
            dir="C:\\songs"
            songs=os.listdir(dir)
            os.startfile(os.path.join(dir,songs[0]))
        elif 'open paint' in query:
            speak('opning ms paint')
            p="C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(p)
        elif 'ms word' in query:
            speak('opening microsoft word 2007')
            word='C:\\Users\\HP\\Desktop\\Microsoft Office Word 2007'
            os.startfile(word)
        elif 'open notepad' in query:
            speak('opening notepad')
            note="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(note)
        elif 'open excel' in query:
            speak('opening excel')
            excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
            os.startfile(excel)
        elif 'open powerpoint' in query:
            speak('opening powerpoint')
            slides="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
            os.startfile(slides)
        elif 'open msaccess' in query:
            speak('opening msaccess')
            access="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007"
            os.startfile(access)
        elif 'open anydesk' in query:
            speak('opening anydesk')
            desk="C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
            os.startfile(desk)
        elif 'open command prompt' in query:
            prompt= "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"

            speak('opening command prompt')
            os.startfile(prompt)
        

            
        elif 'email to smita' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')
        elif 'email to smitha' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')
        
        elif 'email to ismita' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='smitaspn08@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
    
     
            except Exception as e:
                print(e)
                speak('sorry mam, i am not able to send email')


        elif 'activate calculator':
            speak('activating calculator')
            
        my_string=takeCommand()
        print(my_string)
        def get_operator_fn(op):

            return {
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                }[op]
        def eval_binary_expr(op1, oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        result=eval_binary_expr(*(my_string.split()))
        res=print('the result is',result)
        speak(result)
    
