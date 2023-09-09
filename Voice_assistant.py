   
from multiprocessing.connection import Client
from pip import main
from datetime import timedelta,datetime
from playsound import playsound
import openai
import pywhatkit as pwt   
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install the speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
openai.api_key = "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"
def ChatBot(query):
    models = "text-davinci-003"
    if query == "exit":
        breakpoint
    elif ('what is your name' or 'who are you') in query:
        print("My name is Charlie.     A virtual Bot At your service")
        breakpoint
    elif 'who made you' in query:
        print("Aryan Shubham And sanket made me")
        breakpoint
    else:    
        completion = openai.Completion.create(
            model = "text-davinci-003",
            prompt = query,
            max_tokens = 1024,
            temperature = 0.5,
            n=2,
            stop = None
        )
    response = completion.choices[0].text
    UnboundLocalError
    print(response)
    speak(response)
def sendSsmMessage():
    try:
        message_to_broadcast = "sms message"
        client = Client("AC759b0036819d6cbeb2642776ec6c2be8",
                        "eab5f8727089e8ffaa9425af47bd54ec")
        for recipient in ["+918551902607"]:
            if recipient:
                client.messages.create(to=recipient,
                                       from_="settings.TWILIO_NUMBER",
                                       body=message_to_broadcast)
    except ValueError:
        print(ValueError)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    print("Please tell me your name to continue")
    speak("Please tell me your name to continue")
    name1 = takeCommand()
    hour = int(datetime.now().hour)
    if name1 in system_users:
        if hour>=0 and hour<12:
            print("Good Morning",name1,"Welcome")
            speak("Good Morning");speak(name1);speak("Welcome")
            print("How are feeling today sir")
            speak("How are feeling today sir")
            ask_day3 = takeCommand()
            if 'good' or 'nice' or 'fab' in ask_day3:
                print("Nice sir")
                speak("Nice sir")
                print("Lets Make It more nice")
                speak("Lets Make It more nice")
            else:
                speak("No Worries Ok!!")
        elif hour>=12 and hour<18:
            print("Good Afternoon",name1,"Welcome")
            speak("Good Afternoon");speak(name1);speak("Welcome")
            print("So,    How's Your day going?")
            speak("So,    How's Your day going?")
            ask_day2 = takeCommand()
            if 'good' or 'nice' or 'fab' in ask_day2:
                print("Nice sir")
                speak("Nice sir")
                print("Lets Make It more nice")
                speak("Lets Make It more nice")
            else:
                print("Ok No Worries")
                speak("Ok No Worries")
        else:
            print("Good Evening",name1,"Welcome")
            speak("Good Evening");speak(name1);speak("Welcome")
            print("How was your day today?")
            speak("How was your day today?")
            ask_day = takeCommand()
            if 'good' or 'nice' or 'fab'  in ask_day:
                print("Sounds Good!!")
                speak("Sounds Good!!")
            elif('bad' or 'not good') in ask_day:
                print("No Worries. It's All right   Ok!")
                speak("No worries. It's All right   Ok!")
                print("Tomorrow is Your Day. Enjoy that!!")
                speak("Tomorrow is Your Day. Enjoy that!!")
            else:
                print("Ok Sir")
                speak("Ok Sir")
        print("Please tell me how may I help you") 
        speak("Please tell me how may I help you") 
    else:
        print("So you Are a new user.")
        speak("So you Are a new user.")
        print("Please Wait for Initializing the System")
        speak("Please Wait for Initializing the System")
        speak("")
        speak("")
        speak("")
        if hour>=0 and hour<12:
            speak("Alright. Hello Good Morning")
        elif hour>=12 and hour<18:
            speak("Alright. Hello Good Afternoon") 
        else:
            speak("Alright. Hello Good Evening")  
        print("My name is Charlie. Please tell me how may I help you")
        speak("My name is Charlie. Please tell me how may I help you")      
def takeCommand():
    #It takes the microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        speak("Sorry i couldn't hear that")
        takeCommand()
    return query
def takeCommand_initial():
    #It takes the microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        takeCommand_initial()
    return query
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aryanb4112003@gmail.com', 'ylbmlhcvvowifhph')
    server.sendmail('aryanb4112003@gmail.com', to, content)
    server.close()
dict_of_Music = {'past life':'C:\\Users\\Aryan Bhosale\\Downloads\\Music\\Past Lives.mp3',
                 'Blue Eyes':'C:\\Users\\Aryan Bhosale\\Downloads\\Music\\Blue Eyes 3.mp3'}
dict_of_mails = {"aryan":"aryan4112003@gmail.com",
                 "sanket":"sanketsj21hcompe@student.mes.ac.in",
                 "sandeep":"sandeepbhosale2010@gmail.com",
                 "ekta":"mansikale665@gmail.com",
                 "praveen mama":"pravinkamble2612@gmail.com"}
contacts1 = {"aryan":"9324882407",
            "sandeep":"9322133528",
            "shubham":"9372834067",
            "sanket":"7219412617",
            "ekta":"7820955509"}

system_users = {"Aryan","Shubham","Sanket"}

decision = ('wikipedia','what is your name','who are you',"who created you",
            'open youtube','open google','open stackoverflow','play music',
            "what is the time",'open visual studio code','send a mail','sing','send a message','play a song')

# Main Code 
def Charlie007():
    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            try:
                query = takeCommand().lower()
            except:
                query = takeCommand().lower()
            # Logic for executing tasks based on query

            if "sleep" in query:
                speak("Ok sir. Just call my name in need")
                unlock()
            if "thank you" in query:
                speak("My Pleasure. Just call my name in need")
                unlock_moment()

            if ('play a song' or 'sing') in query:
                print("Which song sir ?")
                speak("Which song sir ?")
                song = takeCommand()
                if song in dict_of_Music:
                    speak("ok sir")
                    playsound(dict_of_Music[song])
                else:
                    speak("sorry sir this song is not there in your Music list")
            if 'wikipedia' in query:
                print('Searching Wikipedia...')
                speak('Searching Wikipedia...')
                # query = query.replace("wikipedia", "")
                # results = wikipedia.summary(query, sentences=2)
                # speak("According to Wikipedia")
                # print(results)
                # speak(results)
                voice = pyttsx3.init()
                print("Please tell me, What do you have to search?")
                speak("Please tell me, What do you have to search?")
                try:
                    In = takeCommand().lower()
                except:
                    print("Please tell properly what do have to search?")
                    speak("Please tell properly what do have to search?")
                    In = takeCommand().lower()
                print("According to Wikipedia")
                speak("According to Wikipedia")
                result = wikipedia.summary(In, sentences = 3)
                print(result)
                voice.say(result)
                voice.runAndWait()
            elif ('what is your name') in query:
                print("My name is Charlie. A virtual Bot At your service")
                speak("My name is Charlie. A virtual Bot At your service")
            elif 'who are you' in query:
                print("My name is Charlie. A virtual Bot At your service")
                speak("My name is Charlie. A virtual Bot At your service")
            elif 'who created you' in query:
                print("ARYAN, SHUBHAM And SANKET created me")
                speak("ARYAN, SHUBHAM And SANKET created me")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")  
            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'what is the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            elif 'open visual studio code' in query:
                codePath = "C:\\Users\\Student\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codePath)
            elif 'send a mail' in query:
                try:
                    print("of course sir, Please tell the name of the person to which you have to send the mail")
                    speak("of course sir")
                    speak("Please tell the name of the person to which you have to send the mail")
                    to = takeCommand().lower()
                    if to in dict_of_mails:
                        print("What will be the subject ?")
                        speak("What will be the subject ?")
                        try:
                            subject = takeCommand().upper()
                        except:
                            print("please tell the subject properly")
                            speak("please tell the subject properly")
                            subject = takeCommand().upper()
                        print("What should I write ?")
                        speak("What should I write ?")
                        content = takeCommand().lower()
                        content = "Subject:{}\n\n{}".format(subject,content)
                        sendmail(dict_of_mails[to], content)
                        print("Email has been sent!")
                        speak("Email has been sent!")
                    else:
                        print("Sorry sir, there is no contact of this name in your mail directory")
                        speak("Sorry sir, there is no contact of this name in your mail directory")
                        print("Do you have to add this contact in your mail directory ?")
                        speak("Do you have to add this contact in your mail directory ?")
                        decide_to_add_mail = takeCommand().lower()
                        if decide_to_add_mail == "yes":
                            print("Sir Please tell the mail ID of",to)
                            speak("Sir Please tell the mail ID of");speak(to)
                            dict_of_mails[to] = takeCommand().lower()
                            print("Sir the mail is added in your mail directory.")
                            speak("Sir the mail is added in your mail directory.")
                            print(dict_of_mails)
                            print("now do you have to mail to",to)
                            speak("now do you have to mail to");speak(to)
                            decide_to_add_mail2 = takeCommand().lower()
                            if decide_to_add_mail2 == "yes":
                                print("What will be the subject ?")
                                speak("What will be the subject ?")
                                try:
                                    subject = takeCommand().upper()
                                except:
                                    print("please tell the subject properly")
                                    speak("please tell the subject properly")
                                    subject = takeCommand().upper()
                                print("What should I write ?")
                                speak("What should I write ?")
                                content = takeCommand().lower()
                                content = "Subject:{}\n\n{}".format(subject,content)
                                sendmail(dict_of_mails[to], content)
                                print("Email has been sent!")
                                speak("Email has been sent!")
                            elif decide_to_add_mail2 == "no":
                                breakpoint
                        else:
                            print("Sorry sir the mail contact is not added properly")
                            speak("Sorry sir the mail contact is not added properly")
                except Exception as e:
                    print(e)
                    print("Sorry . I am not able to send this email")
                    speak("Sorry . I am not able to send this email")
            elif 'send a message' in query:
                print("of course sir")
                speak("of course sir")
                print("please tell the name of the person to which you have to send the message")
                speak("please tell the name of the person to which you have to send the message")
                try:
                    name = takeCommand().lower()
                except:
                    print("Please tell the name again properly sir")
                    speak("Please tell the name again properly sir")
                    name = takeCommand().lower()
                print("you have to send the message to ",name)
                speak("you have to send the message to ")
                speak(name)
                if name in contacts1:
                    print("the number of ",name,"is")
                    speak("the number of ")
                    speak(name)
                    speak("is")
                    print(contacts1[name])
                    speak(contacts1[name])
                    print("please tell the message to send to",name)
                    speak("please tell the message to send to");speak(name)
                    try:
                        msg = takeCommand().lower()
                    except:
                        print("Actually i can't figured it out. Please tell the message again")
                        speak("Actually i can't figured it out")
                        speak("Please tell the message again")
                        msg = takeCommand().lower()
                    print("Do you have to send the message now ?")
                    speak("Do you have to send the message now ?")
                    try:
                        send_now = takeCommand().lower()
                    except:
                        print("Sir, Do you have to send the message now ?")
                        speak("Sir, Do you have to send the message now ?")
                        send_now = takeCommand().lower()
                    if send_now == "yes":
                        now = datetime.now()
                        now_plus_2 = now + timedelta(minutes=2)
                        print("Ok Sir, your message will be dilivered within a minute")
                        speak("Ok Sir, your message will be dilivered within a minute")
                        pwt.sendwhatmsg("+91"+contacts1[name], msg, now_plus_2.hour, now_plus_2.minute)
                        break
                    else:
                        print("Then please tell the time to send the message in 24 hour system. \nFirst tell hours")
                        speak("Then please tell the time to send the message in 24 hour system")
                        speak("First tell hours")
                        try:
                            hours = takeCommand()
                            h = int(hours)
                        except:
                            print("Please tell the hours again")
                            speak("Please tell the hours again")
                            hours = takeCommand()
                            h = int(hours)
                        print("Now tell minutes")
                        speak("Now tell minutes")
                        try:
                            min = takeCommand()
                            m = int(min)
                        except:
                            print("please tell the minutes again")
                            speak("please tell the minutes again")
                            min = takeCommand()
                            m = int(min)
                        print("Ok Sir, your message will be dilivered within your given time")
                        speak("Ok Sir, your message will be dilivered within your given time")
                        pwt.sendwhatmsg("+91"+contacts1[name], msg, h, m)
                        break
                else:
                    print("Sorry sir, there is no",name,"in your contacts")
                    speak("Sorry sir, there is no");speak(name);speak("in your contacts")
                    print("do you have to add this contact in your contact list")
                    speak("do you have to add this contact in your contact list")
                    try:
                        decide_to_add = takeCommand().lower()
                    except:
                        print("Do you have to add this contact sir?")
                        speak("Do you have to add this contact sir?")
                        decide_to_add = takeCommand().lower()
                    if decide_to_add == "yes": 
                        print("Please tell the number of",name) 
                        speak("Please tell the number of");speak(name)
                        contacts2 = contacts1
                        try:
                            contacts2[name] = takeCommand().lower()
                        except:
                            print("Sir please tell the number of",name)
                            speak("Sir please tell the number of");speak(name)
                            contacts2[name] = takeCommand().lower()  
                        print("sir, The number is added in your contact list ")
                        speak("sir, The number is added in your contact list ")
                        print(contacts2)
                        print("Now do have to send the message to",name)
                        speak("Now do have to send the message to");speak(name)
                        try:
                            decide_to_send_now = takeCommand().lower()
                        except:
                            print("Sir Do you have to send the message to or not")
                            speak("Sir Do you have to send the message to or not")
                            decide_to_send_now = takeCommand().lower()
                        if decide_to_send_now == "yes":
                            print("please tell the message to send to",name)
                            speak("please tell the message to send to");speak(name)
                            try:
                                msg = takeCommand().lower()
                            except:
                                print("Actually i can't figured it out. Please tell the message again")
                                speak("Actually i can't figured it out")
                                speak("Please tell the message again")
                                msg = takeCommand().lower()
                            print("Do you have to send the message right now?")
                            speak("Do you have to send the message right now?")
                            try:
                                send_now = takeCommand().lower()
                            except:
                                print("Sir, Do you have to send the message right now?")
                                speak("Sir, Do you have to send the message right now?")
                                send_now = takeCommand().lower()
                            if send_now == "yes":
                                now = datetime.now()
                                now_plus_2 = now + timedelta(minutes=2)
                                print("Ok Sir, your message will be dilivered within a minute")
                                speak("Ok Sir, your message will be dilivered within a minute")
                                pwt.sendwhatmsg("+91"+contacts2[name], msg, now_plus_2.hour, now_plus_2.minute)
                                break
                            else:
                                print("Then please tell the time to send the message in 24 hour system")
                                speak("Then please tell the time to send the message in 24 hour system")
                                print("First tell hours")
                                speak("First tell hours")
                                try:
                                    hours = takeCommand()
                                    h = int(hours)
                                except:
                                    print("Please tell the hours again")
                                    speak("Please tell the hours again")
                                    hours = takeCommand()
                                    h = int(hours)
                                print("Now tell minutes")
                                speak("Now tell minutes")
                                try:
                                    min = takeCommand()
                                    m = int(min)
                                except:
                                    print("please tell the minutes again")
                                    speak("please tell the minutes again")
                                    min = takeCommand()
                                    m = int(min)
                                print("Ok Sir, your message will be sent within your given time")
                                speak("Ok Sir, your message will be sent within your given time")
                                pwt.sendwhatmsg("+91"+contacts2[name], msg, h, m)
                                breakpoint
                        else:
                            print("OK Sir.")
                            speak("ok sir")
                            breakpoint
                        breakpoint
                    elif decide_to_add == "no":
                        print("OK Sir.")
                        speak("OK sir")
                        breakpoint
            else:
                ChatBot(query)

 
def Charlie():
    if __name__ == "__main__":
        while True:
        # if 1:
            try:
                speak("yes sir. How can i help you")
                query = takeCommand().lower()
            except:       
                query = takeCommand().lower()
            # Logic for executing tasks based on query

            if "sleep" in query:
                speak("Ok sir")
                unlock()
            if "thank you" in query:
                speak("My Pleasure. Just call my name in need")
                unlock_moment()
            
            if ("thank you" and "sleep"):
                speak("welcome sir")

            if ('play a song' or 'sing') in query:
                print("Which song sir ?")
                speak("Which song sir ?")
                song = takeCommand()
                if song in dict_of_Music:
                    speak("ok sir")
                    playsound(dict_of_Music[song])
                else:
                    speak("sorry sir this song is not there in your Music list")
            if 'wikipedia' in query:
                print('Searching Wikipedia...')
                speak('Searching Wikipedia...')
                # query = query.replace("wikipedia", "")
                # results = wikipedia.summary(query, sentences=2)
                # speak("According to Wikipedia")
                # print(results)
                # speak(results)
                voice = pyttsx3.init()
                print("Please tell me, What do you have to search?")
                speak("Please tell me, What do you have to search?")
                try:
                    In = takeCommand().lower()
                except:
                    print("Please tell properly what do have to search?")
                    speak("Please tell properly what do have to search?")
                    In = takeCommand().lower()
                print("According to Wikipedia")
                speak("According to Wikipedia")
                result = wikipedia.summary(In, sentences = 3)
                print(result)
                voice.say(result)
                voice.runAndWait()
            elif ('what is your name') in query:
                print("My name is Charlie. A virtual Bot At your service")
                speak("My name is Charlie. A virtual Bot At your service")
            elif 'who are you' in query:
                print("My name is Charlie. A virtual Bot At your service")
                speak("My name is Charlie. A virtual Bot At your service")
            elif 'who created you' in query:
                print("ARYAN, SHUBHAM And SANKET created me")
                speak("ARYAN, SHUBHAM And SANKET created me")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")  
            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'what is the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            elif 'open visual studio code' in query:
                codePath = "C:\\Users\\Student\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codePath)
            elif 'send a mail' in query:
                try:
                    print("of course sir, Please tell the name of the person to which you have to send the mail")
                    speak("of course sir")
                    speak("Please tell the name of the person to which you have to send the mail")
                    to = takeCommand().lower()
                    if to in dict_of_mails:
                        print("What will be the subject ?")
                        speak("What will be the subject ?")
                        try:
                            subject = takeCommand().upper()
                        except:
                            print("please tell the subject properly")
                            speak("please tell the subject properly")
                            subject = takeCommand().upper()
                        print("What should I write ?")
                        speak("What should I write ?")
                        content = takeCommand().lower()
                        content = "Subject:{}\n\n{}".format(subject,content)
                        sendmail(dict_of_mails[to], content)
                        print("Email has been sent!")
                        speak("Email has been sent!")
                    else:
                        print("Sorry sir, there is no contact of this name in your mail directory")
                        speak("Sorry sir, there is no contact of this name in your mail directory")
                        print("Do you have to add this contact in your mail directory ?")
                        speak("Do you have to add this contact in your mail directory ?")
                        decide_to_add_mail = takeCommand().lower()
                        if decide_to_add_mail == "yes":
                            print("Sir Please tell the mail ID of",to)
                            speak("Sir Please tell the mail ID of");speak(to)
                            dict_of_mails[to] = takeCommand().lower()
                            print("Sir the mail is added in your mail directory.")
                            speak("Sir the mail is added in your mail directory.")
                            print(dict_of_mails)
                            print("now do you have to mail to",to)
                            speak("now do you have to mail to");speak(to)
                            decide_to_add_mail2 = takeCommand().lower()
                            if decide_to_add_mail2 == "yes":
                                print("What will be the subject ?")
                                speak("What will be the subject ?")
                                try:
                                    subject = takeCommand().upper()
                                except:
                                    print("please tell the subject properly")
                                    speak("please tell the subject properly")
                                    subject = takeCommand().upper()
                                print("What should I write ?")
                                speak("What should I write ?")
                                content = takeCommand().lower()
                                content = "Subject:{}\n\n{}".format(subject,content)
                                sendmail(dict_of_mails[to], content)
                                print("Email has been sent!")
                                speak("Email has been sent!")
                            elif decide_to_add_mail2 == "no":
                                breakpoint
                        else:
                            print("Sorry sir the mail contact is not added properly")
                            speak("Sorry sir the mail contact is not added properly")
                except Exception as e:
                    print(e)
                    print("Sorry . I am not able to send this email")
                    speak("Sorry . I am not able to send this email")
            elif 'send a message' in query:
                print("of course sir")
                speak("of course sir")
                print("please tell the name of the person to which you have to send the message")
                speak("please tell the name of the person to which you have to send the message")
                try:
                    name = takeCommand().lower()
                except:
                    print("Please tell the name again properly sir")
                    speak("Please tell the name again properly sir")
                    name = takeCommand().lower()
                print("you have to send the message to ",name)
                speak("you have to send the message to ")
                speak(name)
                if name in contacts1:
                    print("the number of ",name,"is")
                    speak("the number of ")
                    speak(name)
                    speak("is")
                    print(contacts1[name])
                    speak(contacts1[name])
                    print("please tell the message to send to",name)
                    speak("please tell the message to send to");speak(name)
                    try:
                        msg = takeCommand().lower()
                    except:
                        print("Actually i can't figured it out. Please tell the message again")
                        speak("Actually i can't figured it out")
                        speak("Please tell the message again")
                        msg = takeCommand().lower()
                    print("Do you have to send the message now ?")
                    speak("Do you have to send the message now ?")
                    try:
                        send_now = takeCommand().lower()
                    except:
                        print("Sir, Do you have to send the message now ?")
                        speak("Sir, Do you have to send the message now ?")
                        send_now = takeCommand().lower()
                    if send_now == "yes":
                        now = datetime.now()
                        now_plus_2 = now + timedelta(minutes=2)
                        print("Ok Sir, your message will be dilivered within a minute")
                        speak("Ok Sir, your message will be dilivered within a minute")
                        pwt.sendwhatmsg("+91"+contacts1[name], msg, now_plus_2.hour, now_plus_2.minute)
                        break
                    else:
                        print("Then please tell the time to send the message in 24 hour system. \nFirst tell hours")
                        speak("Then please tell the time to send the message in 24 hour system")
                        speak("First tell hours")
                        try:
                            hours = takeCommand()
                            h = int(hours)
                        except:
                            print("Please tell the hours again")
                            speak("Please tell the hours again")
                            hours = takeCommand()
                            h = int(hours)
                        print("Now tell minutes")
                        speak("Now tell minutes")
                        try:
                            min = takeCommand()
                            m = int(min)
                        except:
                            print("please tell the minutes again")
                            speak("please tell the minutes again")
                            min = takeCommand()
                            m = int(min)
                        print("Ok Sir, your message will be dilivered within your given time")
                        speak("Ok Sir, your message will be dilivered within your given time")
                        pwt.sendwhatmsg("+91"+contacts1[name], msg, h, m)
                        break
                else:
                    print("Sorry sir, there is no",name,"in your contacts")
                    speak("Sorry sir, there is no");speak(name);speak("in your contacts")
                    print("do you have to add this contact in your contact list")
                    speak("do you have to add this contact in your contact list")
                    try:
                        decide_to_add = takeCommand().lower()
                    except:
                        print("Do you have to add this contact sir?")
                        speak("Do you have to add this contact sir?")
                        decide_to_add = takeCommand().lower()
                    if decide_to_add == "yes": 
                        print("Please tell the number of",name) 
                        speak("Please tell the number of");speak(name)
                        contacts2 = contacts1
                        try:
                            contacts2[name] = takeCommand().lower()
                        except:
                            print("Sir please tell the number of",name)
                            speak("Sir please tell the number of");speak(name)
                            contacts2[name] = takeCommand().lower()  
                        print("sir, The number is added in your contact list ")
                        speak("sir, The number is added in your contact list ")
                        print(contacts2)
                        print("Now do have to send the message to",name)
                        speak("Now do have to send the message to");speak(name)
                        try:
                            decide_to_send_now = takeCommand().lower()
                        except:
                            print("Sir Do you have to send the message to or not")
                            speak("Sir Do you have to send the message to or not")
                            decide_to_send_now = takeCommand().lower()
                        if decide_to_send_now == "yes":
                            print("please tell the message to send to",name)
                            speak("please tell the message to send to");speak(name)
                            try:
                                msg = takeCommand().lower()
                            except:
                                print("Actually i can't figured it out. Please tell the message again")
                                speak("Actually i can't figured it out")
                                speak("Please tell the message again")
                                msg = takeCommand().lower()
                            print("Do you have to send the message right now?")
                            speak("Do you have to send the message right now?")
                            try:
                                send_now = takeCommand().lower()
                            except:
                                print("Sir, Do you have to send the message right now?")
                                speak("Sir, Do you have to send the message right now?")
                                send_now = takeCommand().lower()
                            if send_now == "yes":
                                now = datetime.now()
                                now_plus_2 = now + timedelta(minutes=2)
                                print("Ok Sir, your message will be dilivered within a minute")
                                speak("Ok Sir, your message will be dilivered within a minute")
                                pwt.sendwhatmsg("+91"+contacts2[name], msg, now_plus_2.hour, now_plus_2.minute)
                                break
                            else:
                                print("Then please tell the time to send the message in 24 hour system")
                                speak("Then please tell the time to send the message in 24 hour system")
                                print("First tell hours")
                                speak("First tell hours")
                                try:
                                    hours = takeCommand()
                                    h = int(hours)
                                except:
                                    print("Please tell the hours again")
                                    speak("Please tell the hours again")
                                    hours = takeCommand()
                                    h = int(hours)
                                print("Now tell minutes")
                                speak("Now tell minutes")
                                try:
                                    min = takeCommand()
                                    m = int(min)
                                except:
                                    print("please tell the minutes again")
                                    speak("please tell the minutes again")
                                    min = takeCommand()
                                    m = int(min)
                                print("Ok Sir, your message will be sent within your given time")
                                speak("Ok Sir, your message will be sent within your given time")
                                pwt.sendwhatmsg("+91"+contacts2[name], msg, h, m)
                                breakpoint
                        else:
                            print("OK Sir.")
                            speak("ok sir")
                            breakpoint
                        breakpoint
                    elif decide_to_add == "no":
                        print("OK Sir.")
                        speak("OK sir")
                        breakpoint
            else:
                ChatBot(query)


def unlock():
    answer = takeCommand_initial()
    if "Charlie" in answer:
        speak("Hello")
        Charlie007()
    elif "Wake up" in answer:
        speak("Hello")
        Charlie007()
    elif "wake" in answer:
        speak("Hello")
        Charlie007()
    else:
        unlock()
def unlock_moment():
    answer = takeCommand_initial()
    if "Charlie" in answer:
        Charlie()
    elif "Wake up" in answer:
        Charlie()
    elif "wake" in answer:
        Charlie()
    else:
        unlock_moment()

unlock()
        
