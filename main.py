"""
Created on sunday jan  5 20:19:47 2020

@author: Akash B, 
"""

from tkinter import *
import tkinter as tk          
from tkinter import messagebox, Frame, Label, Button, Entry      
from tkinter import font  as tkfont 
from tkinter import messagebox as tm

import sys

import smtplib
from smtplib import SMTPException
import tkinter as tk
from tkinter import Message ,Text
from tkinter import messagebox as tm
import os
import csv
from datetime import date
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import urllib
import urllib.request as ur
c1=0
c="orange"
w="white"



class college(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("DOCmate")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (loginPage,StartPage,Atendance,smartclass,Timetable):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("loginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def clear(self):
        txt.delete(0, 'end')    
        res = ""
        message.configure(text= res)

    def clear2(self):
        txt2.delete(0, 'end')    
        res = ""
        message.configure(text= res)    
    
    def is_number(self,s):
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
 






    def sms(self):
        account_sid = 'AC5d77f2b98cac78c31bfefbe9098a5566'
        auth_token = 'b553f334ef0eacfb858f9149a2c1ad5e'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                      body='Your Son/Doughter Absent Today',
                                      from_='+12512570587',
                                      to='+919080069305'
                                  )
        playsound("sms.mp3")


 

      
             
    

    
class loginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        
        load = Image.open("tech.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "left", fill = "y", expand = "yes")
        img.image = render
        img.place(x=0, y=0)

        


        self.title_1 = tk.Label(self, text="SMART HOME CITY",font=("Verdana", 35))
        self.title_1.place(x=500, y=150)
        self.title_1.pack(side="top", fill="x", pady=50)

        self.label_1 = tk.Label(self, text="Username:" ,font=("Verdana", 12))
        self.label_1.place(x=500, y=200)

        self.entry_1 = tk.Entry(self,font=("Verdana", 10))
        self.entry_1.place(x=600, y=200)

        self.label_2 = tk.Label(self, text="Password:",font=("Verdana", 12))
        self.label_2.place(x=500, y=250)
        
        self.entry_2 = tk.Entry(self, show="hjcjcvjhvk",font=("Verdana", 10))
        self.entry_2.place(x=600, y=253)

        self.logbtn = tk.Button(self, text="Login", command=self._password_check, font=("Verdana", 10), width=14, relief=GROOVE)
        self.logbtn.place(x=600, y=293)
        #lambda: controller.show_frame("StartPage")
        

    def _password_check(self):
        print("Clicked")

        username = self.entry_1.get()
        password = self.entry_2.get()
        print(username, password)

        if username == "admin" and password == "password":
            app.show_frame("StartPage")
        elif username == "user" and password == "password":
            app.show_frame("Atendance")
        else:
            tm.showerror("Login error", "Incorrect username or password")
            
            
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='aquamarine')


        load = Image.open("te.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "left", fill = "y", expand = "yes")
        img.image = render
        img.place(x=0, y=0)
        datee = tk.Label(self, text="",borderwidth=4, relief="solid" ,fg="red",bg=w,activeforeground = "green",width=20  ,height=2  ,font=('times', 15, ' bold ')) 
        datee.place(x=0, y=0)

        today = date.today()
        datee.configure(text=today)

        
        message = tk.Label(self, text="SMART - HOME  CITY" ,bg=c  ,fg="black"  ,width=35  ,height=1,font=('times', 30, 'italic bold underline')) 

        message.place(x=250, y=0)

        quitt = tk.Button(self, text="Quit", command=self.destroy  ,fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitt.place(x=1000, y=600)

        nextt = tk.Button(self, text="NextPage", command=lambda:controller.show_frame("Timetable"),fg="red"  ,bg=c  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        nextt.place(x=1300, y=600)
          

class Atendance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        load = Image.open("jsrr3.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "left", fill = "y", expand = "yes")
        img.image = render
        img.place(x=0, y=0)
        c="orange"
        w="white"
       
        

class smartclass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller   



        load = Image.open("jsrr6.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "left", fill = "y", expand = "yes")
        img.image = render
        img.place(x=0, y=0)
        c="orange"
        w="white"


        datee = tk.Label(self, text="",borderwidth=4, relief="solid" ,fg="red"   ,bg=w,activeforeground = "green",width=20  ,height=2  ,font=('times', 15, ' bold ')) 
        datee.place(x=10, y=10)

        today = date.today()
        datee.configure(text=today)

       
        


     
    
    
        button = tk.Button(self,text="Back",command=lambda: controller.show_frame("StartPage"))
        button.pack()


        
        
class Timetable(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller   



        load = Image.open("time.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "left", fill = "y", expand = "yes")
        img.image = render
        img.place(x=0, y=0)


        datee = tk.Label(self, text="",borderwidth=4, relief="solid" ,fg="red"   ,bg=w,activeforeground = "green",width=20  ,height=2  ,font=('times', 15, ' bold ')) 
        datee.place(x=10, y=10)

        today = date.today()
        datee.configure(text=today)
        
        quitt = tk.Button(self, text="QUIT", command=self.destroy  ,fg="red"  ,bg="white"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitt.place(x=1200, y=700)
          

        

        
        
        
if __name__ == "__main__":
    app = college()
    
    app.geometry('1800x900')
    app.mainloop()
        
        
        
        
        
