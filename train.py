# -*- coding: utf-8 -*-
"""
Created on tue JULY 30 2019

@author: AKASH,JOTHI,GOWTHAM
"""

import tkinter as tk
from tkinter import Message ,Text
from tkinter import messagebox as tm
import cv2
import os
import easyimap
from gtts import gTTS 
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as p
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from twilio.rest import Client
window = tk.Tk()
from playsound import playsound
import easyimap
import urllib
import urllib.request as ur






window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
 
window.geometry('1920x1080')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

path = "jsrr3.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)

panel.pack(side = "left", fill = "y", expand = "yes")
c="orange"
w="white"



message = tk.Label(window, text="Smart-Attendance-Using-Facial-Recognition" ,bg=c  ,fg="black"  ,width=50  ,height=1,font=('times', 30, 'italic bold underline')) 

message.place(x=200, y=0)

lbl = tk.Label(window, text="Enter ID",borderwidth=4, relief="solid",width=20  ,height=2  ,fg="red"  ,bg=c ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)

txt = tk.Entry(window,width=25,bg=w ,fg="red",font=('times', 15, ' bold '))
txt.pack(ipady=10)
txt.place(x=300, y=215)

lbl2 = tk.Label(window, text="Enter Name",borderwidth=4, relief="solid",width=20  ,fg="red"  ,bg=c    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=10, y=300)

txt2 = tk.Entry(window,width=25  ,bg=w ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=300, y=315)

lbl3 = tk.Label(window, text="Notification : ",borderwidth=4, relief="solid",width=20  ,fg="red"  ,bg=c  ,height=2 ,font=('times', 15, ' bold underline ')) 
lbl3.place(x=10, y=400)

message = tk.Label(window, text="",borderwidth=4, relief="solid" ,bg=w ,fg="red"  ,width=44  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=300, y=400)

lbl3 = tk.Label(window, text="Attendance : ",borderwidth=4, relief="solid",width=20  ,fg="red"  ,bg=c  ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl3.place(x=10, y=500)

message3 = tk.Label(window, text="",borderwidth=4, relief="solid" ,bg=w ,fg="red"  ,width=25  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message3.place(x=1000, y=200)


message2 = tk.Label(window, text="",borderwidth=4, relief="solid" ,fg="red"   ,bg=w,activeforeground = "green",width=44  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=300, y=500)

lbl4=tk.Label(window,text="Developed By : Akash.B,JothiPrakash.V,Gowtham.N.S",fg="black"   ,bg=c,activeforeground = "green",width=45  ,height=2  ,font=('times', 20, ' bold '))
lbl4.place(x=840,y=725)
 
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)

    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trainner.yml")
    res = "Image Trained"
    message.configure(text= res)

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 

    faces=[]
 
    Ids=[]
    for imagePath in imagePaths:

        pilImage=Image.open(imagePath).convert('L')

        imageNp=np.array(pilImage,'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
 
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                playsound("present.mp3")
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    print(attendance)
    res=attendance
    message2.configure(text= res)


`
def msg():
    

    email_user = 'jsrrengineeringcollegge@gmail.com'
    email_password = 'cseuser!'
    email_send = "babushanthi207@gmail.com"

    subject = 'CSE III year Attendace'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'THIS IS FROM CSE A ATTENDENCE DETAIL'
    msg.attach(MIMEText(body,'plain'))

    filename='atendance.csv'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    playsound("good.mp3")
    
    server.quit()

   
def sms():
  



def newmail():
    imapper = easyimap.connect('imap.gmail.com', login, password)
    for mail_id in imapper.listids(limit=2):
        mail = imapper.mail(mail_id)
        #print(mail.from_addr)
        #print(mail.to)
        #print(mail.cc)
        t=mail.title
        m=mail.body
            
        language = 'en'
        myobj = gTTS(text=m, lang=language, slow=False)
        tm.showinfo(t,m)
        myobj.save("circular.mp3")
        playsound("circular.mp3")



        #print(mail.attachments)
        

def general():
    """f=open("general.txt", "r")

    t=f.read()
    language = 'en'
    myobj = gTTS(text=t, lang=language, slow=False) 
    myobj.save("general.mp3")"""
    playsound("general.mp3")
"""class time():
    def __init__():
        canvas = tk.Canvas(root, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("time.png"))  
        canvas.create_image(20, 20, anchor=NW, image=img)  """
        


clearButton1 = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton1.place(x=590, y=200)


sms = tk.Button(window, text="sms", command=sms ,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
sms.place(x=10, y=700)

General= tk.Button(window, text="General Qns", command= general,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
General.place(x=850, y=500)


#time= tk.Button(window, text="Time Table", command=sms,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
#time.place(x=1140, y=500)

Circular= tk.Button(window, text="Circular", command=newmail  ,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
Circular.place(x=850, y=600)


mail = tk.Button(window, text="Mail", command=msg  ,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
mail.place(x=590, y=700)

live = tk.Button(window, text="live", command=live  ,fg="red"  ,bg=c  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
live.place(x=1140, y=600)

clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=590, y=300)    
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=10, y=600)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=300, y=600)
trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=590, y=600)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=300, y=700)
playsound("JSRR.mp3")




window.mainloop()
