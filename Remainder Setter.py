from datetime import datetime
import speech_recognition as sr
a=sr.Recognizer()
import pyttsx3 as r
engine = r.init()
engine.setProperty("rate",140)
mon={"january":"01",'february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12'}

def speak(n):
    engine.say(n)
    engine.runAndWait()
    
def time_():
    speak("please tell me the time in order to remaind you")
    while True:
        time=reg()
        print(time)
        if len(time)==9:
            return time
            break
        else:
            print(time)
            speak("something went wrong please repeate the timing of the remainder")
            
def reg():
    with sr.Microphone() as speech:
        speak("listening")
        while True:
            try:
                a.adjust_for_ambient_noise(speech)
                spoke=a.listen(speech)
                text=a.recognize_google(spoke)
                speak("copied")
                return text
                break
            except:
                continue
speak("say set remainder, or remind me, in order to set remainder")
text=reg()
if text.lower()=="set reminder" or text.lower()=="remind me" or text.lower()=="set remainder":
    speak("please tell me the remainding date")
    text=reg()
    date,month,year=text.split()
    time=time_()
    speak("what would you want me to remaind")
    remain=reg()
    speak("is that "+remain)
    con=reg()
    if con.lower()=="no":
        speak("please tell me the remainder again")
        remain=reg()
    f=open("E:\AJ_Mark_II\Remainder\Remainder Dataset.txt",'a')
    f.write(date+"."+mon[month.lower()]+"."+year+" "+time+" "+remain+"\n")
    f.close()
    speak("remainder is set")
else:
    speak("thank you sir")

