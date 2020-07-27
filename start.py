#!/usr/bin/env python3                                                                                

import serial
import time
import speech_recognition as sr  

# get audio from the microphone
port = '/dev/cu.usbmodem142101'                                                                  
r = sr.Recognizer()
started = True
ser = serial.Serial(port, 9600, timeout=0.5)
def Send(msg):
    msg = msg.encode()
    
    ser.flushInput()
    ser.write(msg)
    time.sleep(1)
    x=ser.readline()
    print(str(x))
    ser.close()


while started:

    with sr.Microphone() as source:                                                                       
        print("Speak:")
        audio = r.listen(source, phrase_time_limit=2)

    try:
        print(r.recognize_google(audio))
        text = r.recognize_google(audio)
        
        if text == "fridge open":
            print("opening fridge...")
            Send("open")
        elif text == "fridge close":
            print("closing fridge")
            Send("close")
        elif text == "fridge stop":
            print("stoping the fridge")
            Send("stop")
        elif text == "stop program":
            print("stoping the program")
            started = False
            
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

