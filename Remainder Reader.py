from datetime import datetime
import random
from playsound import playsound
import pyttsx3 as r
engine = r.init()
engine.setProperty("rate",120)

def speak(n):
    engine.say(n)
    engine.runAndWait()
    
day,time=str(str(datetime.now()).split("(")).split()
day=day.replace("['","")
time=time.split(".")[0]
y,m,d=day.split("-")
f_r=open("E:\AJ_Mark_II\Remainder\Remainder Dataset.txt","r")
l=f_r.readlines()
f_r.close()
u_l=[]
c=0
mon={'01':" january ",'02':' february ','03':' march ','04':' april ','05':' may ','06':' june ','07':' july ','08':' august ','09':' september ','10':' october ','11':' november ','12':' december '}
res=["hai sir","hello sir","sir"]
abt=["insisted","ordered","told "]

for i in l:
    date,time_,sess,con=i.split(" ",3)
    if int(date.split(".")[2])<int(y):
        c+=1
        break
    elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])<int(m):
        c+=1
        break
    elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])==int(m) and int(date.split(".")[0])<int(d):
        c+=1
        break
    elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])==int(m) and int(date.split(".")[0])==int(d):
        h,m_s=time_.split(":",1)
        if sess=="p.m.":
            h=int(h)+12
        if h<int(time.split(":")[0]):
            c+=1
            break
        elif h==int(time.split(":")[0]) and int(m_s)<int(time.split(":")[1]):
            c+=1
            break
if c>0:
    j=0
    while j<3:
        playsound("E:/AJ_Mark_II/Remainder/beep-07.mp3")
        j+=1
    speak(random.choice(res)+" , you have a missed remainders")
    k=1
    for i in l:
        c=0
        date,time_,sess,con=i.split(" ",3)
        if int(date.split(".")[2])<int(y):
            c+=1
            speak("number "+str(k)+" , "+con+" "+", you "+random.choice(abt)+" me to remaind this on , "+str(date.split(".")[0])+mon[str(date.split(".")[1])]+str(date.split(".")[2]))
            k+=1
        elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])<int(m):
            c+=1
            speak("number "+str(k)+" , "+con+" "+", you "+random.choice(abt)+" me to remaind this on , "+str(date.split(".")[0])+mon[str(date.split(".")[1])]+str(date.split(".")[2]))
            k+=1
        elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])==int(m) and int(date.split(".")[0])<int(d):
            c+=1
            speak("number "+str(k)+" , "+con+" "+", you "+random.choice(abt)+" me to remaind this on , "+str(date.split(".")[0])+mon[str(date.split(".")[1])]+str(date.split(".")[2]))
            k+=1
        elif int(date.split(".")[2])==int(y) and int(date.split(".")[1])==int(m) and int(date.split(".")[0])==int(d):
            h,m_s=time_.split(":",1)
            if sess=="p.m.":
                h=int(h)+12
            if h<int(time.split(":")[0]):
                c+=1
                speak("number "+str(k)+" , "+con+" "+", you "+random.choice(abt)+" me to remaind this on , "+str(date.split(".")[0])+mon[str(date.split(".")[1])]+str(date.split(".")[2]))
                k+=1
            elif h==int(time.split(":")[0]) and int(m_s)<int(time.split(":")[1]):
                c+=1
                speak("number "+str(k)+" , "+con+" "+", you "+random.choice(abt)+" me to remaind this on , "+str(date.split(".")[0])+mon[str(date.split(".")[1])]+str(date.split(".")[2]))
                k+=1
        if c==0:
            u_l.append(i)
    if len(u_l)!=5:
        f_r=open("E:\AJ_Mark_II\Remainder\Remainder Dataset.txt","w")
        for i in u_l:
            f_r.write(i+"\n")
        f_r.close()
while True:
    day,time=str(str(datetime.now()).split("(")).split()
    day=day.replace("['","")
    time=time.split(".")[0]
    y,m,d=day.split("-")
    u_r=[]
    c=0
    f_r=open("E:\AJ_Mark_II\Remainder\Remainder Dataset.txt","r")
    z=f_r.readlines()
    f_r.close()
    for i in z:
        date,time_,sess,con=i.split(" ",3)
        d_,m_,y_=date.split(".")
        if int(y_)==int(y) and int(m_)==int(m) and int(d_)==int(d):
            h,m_s=time_.split(":",1)
            if sess=="p.m.":
                h=int(h)+12
            if h==int(time.split(":")[0]) and int(m_s)==int(time.split(":")[1]):
                j=0
                while j<3:
                    playsound("E:/AJ_Mark_II/Remainder/beep-07.mp3")
                    j+=1
                speak(random.choice(res)+" , you "+random.choice(abt)+" me to remaind regarding "+con)            
                c+=1
            else:
                u_r.append(i)
    if c>0:
        f_w=open("E:\AJ_Mark_II\Remainder\Remainder Dataset.txt","w")
        for i in u_r:
            f_w.write(i+"\n")
        f_w.close()
