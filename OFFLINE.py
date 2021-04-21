## 1. Import
import tkinter
from tkinter import *
import pyttsx3
from pyttsx3 import Engine

## 2. Initializing  the window pompt as GUI
root = tkinter.Tk()
root.geometry('300x600')
root.configure(bg='ghost white')
root.title("MINI_PROJECT(BATCH-18)-TEXT_TO_SPEECH")
bi = PhotoImage(file="C:\\users\\NM RAJU\\Desktop\\prj img\\sam.png")
tkinter.Label(root, image=bi).place(x=0, y=0, relwidth=1, relheight=1)
tkinter.Label(root, text="TEXT_TO_SPEECH", font="arial 20 bold", bg='white smoke').pack()
tkinter.Label(text="MINI_PROJECT", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')

# 3.Initialize pyttsx3 engine for convert this text to speech

def OFFLINE():
    engine: Engine = pyttsx3.init()
    Message = entry_field.get()
    engine.say(Message)
    engine.runAndWait()

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# 4.Initialize Buttons and text entry filed  , giving command to the Buttons and text entry filed

tkinter.Button(root, text="PLAY", font='arial 15 bold', command=OFFLINE, width='6').place(x=100, y=350)

tkinter.Button(root, font='arial 15 bold', text='EXIT', width='6', command=Exit, bg='OrangeRed1').place(x=100,
                                                                                                        y=400)
tkinter.Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=100, y=450)
Msg = tkinter.StringVar()
tkinter.Label(root, text="Enter Text", font='arial 18 bold', bg='white smoke').place(x=60, y=200)

entry_field = tkinter.Entry(root, textvariable=Msg, width='30', bg='white smoke')
entry_field.place(x=56, y=250)
root.mainloop()


