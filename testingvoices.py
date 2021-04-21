## 1. Import
import tkinter
from tkinter import *
import pyttsx3
from pyttsx3 import Engine
'''
v = Engine.getProperty('voice')
Engine.setProperty('voice', voices[0])
Engine.setProperty('rate',150)
Engine.say ("hello")
Engine.runAndWait()
'''

Engine: Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')

Engine.setProperty('voice', voices[1].id)  # changes the voice
Engine.say('The quick brown fox jumped over the lazy dog.')
Engine.runAndWait()
'''
Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
print(voices)
'''