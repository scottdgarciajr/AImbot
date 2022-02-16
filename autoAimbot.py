#Scott's First AI Aimbot
import pyautogui
import cv2
import os
import time
import threading
from pynput.keyboard import Listener, KeyCode
import pydirectinput
from PIL import ImageGrab



start_stop_key = KeyCode(char='z')
snap_key = KeyCode(char='x')
exit_key = KeyCode(char='0')
delay = 0.0333333333
face_cascade = cv2.CascadeClassifier('C:\\Users\\scott\\OneDrive\\Desktop\\Python Codeses thingses\\haarcascade_frontalface_default.xml')
    


def aim():
    #Code to detect faces draw box and move mouse to it
    myScreenshot = ImageGrab.grab()
    myScreenshot.save(r'C:\Users\scott\OneDrive\Desktop\Python Codeses thingses\aimbotMemory\snap.jpg')
    img = cv2.imread('C:\\Users\\scott\\OneDrive\\Desktop\\Python Codeses thingses\\aimbotMemory\\snap.jpg')
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        pydirectinput.moveTo(x,y) 
       # print(str(x)+", " + str(y))
       # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)
    
    #cv2.imwrite("C:\\Users\\scott\\OneDrive\Desktop\\Python Codeses thingses\\aimbotMemory\\face_detected.jpg", img) 
                
aiming = False         


def on_press(key):
    if key == start_stop_key:

        print('oops')
            
    elif key == snap_key:
      aim()  
    elif key == exit_key:
        exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()



