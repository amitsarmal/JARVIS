import pyttsx3  # text to speech convert
import speech_recognition as sr  # to recognize user’s voice
import datetime   # for date,time related information
import wikipedia 
import webbrowser   
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():         # To wish according to time 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour< 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  

    speak("I am you assistant Sir. Please tell me how may I help you")   
       

def takeCommand():
    """It takes microphone input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 5)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        user_input = r.recognize_google(audio, language='en-in')
        print(f"User said: {user_input}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return user_input

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ue198015@gmail.com', 'password')
    server.sendmail('ue198015@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        user_input = takeCommand().lower()

        # Execution depending on user_input
        if 'wikipedia' in user_input:
            speak('Searching Wikipedia...')
            user_input = user_input.replace("wikipedia", "")
            results = wikipedia.summary(user_input, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in user_input:
            webbrowser.open("youtube.com")

        elif 'open google' in user_input:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in user_input:
            webbrowser.open("stackoverflow.com")   


        elif 'play movie' in user_input:
            music_dir = 'D:\\movies'    # insert file path according to movies folder
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in user_input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'email to amit' in user_input:   # to send mail to amit
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ue198015@gmail.com"    # email id of amit
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")  




