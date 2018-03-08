a1='Hello There! This is a simple chatting bot created by Sandeep Sharma'
a2='What would you like to do?'
from gtts import gTTS
import speech_recognition as sr
import os
import pyttsx3
eng=pyttsx3.init()
print(a1)
eng.say(a1)
eng.runAndWait()
print(a2)
eng.say('so'+a2)
eng.runAndWait()
def mycommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_thresold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        command=r.recognize_google(audio)
        if command=='bye':
            exit()
        else:
            print('You said : ' + command)
            eng.say('you said'+ command)
            eng.runAndWait()
    #loop back to continue to listen commands

    except sr.UnknownValueError:
        mycommand()
    return 0
ch=mycommand()

while True:
    mycommand()
