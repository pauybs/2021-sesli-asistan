# -*- coding: utf-8 -*-


import speech_recognition as sr
from datetime import datetime
from playsound import playsound
from gtts import gTTS
import random
import os
import untitled4
import time
import bluetooth

r = sr.Recognizer()
mic = sr.Microphone()
sock = ''


    
def arduino_connect_lamba():
    global sock
    print("searching for devices...")
    nearby_devices = bluetooth.discover_devices()
    num = 0
    for i in nearby_devices:
        num+=1
        print(str(num)+":"+bluetooth.lookup_name(i)+" MAC: "+i)
        if i=="20:18:07:13:70:0B":
            selection = num-1
    bd_addr = nearby_devices[selection]
    port = 1
    print("You have selected :" +bluetooth.lookup_name(bd_addr))
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
    
def arduino_connect_kapi():
    global sock
    print("searching for devices...")
    nearby_devices = bluetooth.discover_devices()
    num = 0
    for i in nearby_devices:
        num+=1
        print(str(num)+":"+bluetooth.lookup_name(i)+" MAC: "+i)
        if i=="00:20:10:08:79:23":
            selection = num-1
    bd_addr = nearby_devices[selection]
    port = 1
    print("You have selected :" +bluetooth.lookup_name(bd_addr))
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
        
def mic_text_doc():
    text = ''
    with mic as m:
        print("seni dinliyorum")
        audio = r.listen(m, phrase_time_limit = 4)
        try:
            text = r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            print("----seni anlayamadım---")
    return text

def arduino_gonder(x):
    global sock
    if sock != '':
        sock.send(x)
    else:
        print("bağlantı yok")

def arduino_oku():
    global sock
    time.sleep(0.5)
    try:
        while True:
            data = sock.recv(4096)
            data = data.decode("utf-8")
            if "!" in data:
                break
    except:
        print(data,"---")
    print(data)
    
try:
    while True:
        text = mic_text_doc().lower()
        if "asistan" in text:
             
            if "lamba aç" in text:
                if sock != '':
                    sock.getsockname()
                    sock.getpeername()
                    sock.close()
                else:
                    print("bağlantı zaten yok")
                arduino_connect_lamba()
                arduino_gonder("f")               
                pass
            
            elif "lamba kapat" in text:
                arduino_gonder("g")           
                pass
            
            elif "kapıyı aç" in text:                                
                arduino_gonder("g")               
                pass
            
            elif "kapıyı kilitle" in text:
                if sock != '':
                    sock.getsockname()
                    sock.getpeername()
                    sock.close()
                else:
                    print("bağlantı zaten yok")
                arduino_connect_kapi()
                arduino_gonder("f")               
                pass
            
            elif "bağlantıyı kapat" in text:
                if sock != '':
                    sock.getsockname()
                    sock.getpeername()
                    sock.close()
                else:
                    print("bağlantı zaten yok")
                
        elif "uygulamadan çık" in text:      
            if sock != '':
                    sock.getsockname()
                    sock.getpeername()
                    sock.close()
            break
        else:
            pass

except KeyboardInterrupt:
    if sock != '':
        sock.getsockname()
        sock.getpeername()
        sock.close()
    print("uygulama klavye ile kapatıldı..")
    pass

