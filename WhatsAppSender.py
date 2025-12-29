import time
import pyautogui
import keyboard as k
import datetime
import pywhatkit as pwk


def sendMsgonWA(message,mobilenumber):  
   
        
 
    datet=str(datetime.datetime.now())
    st=datet.split(" ")
    kt=st[1].split(":")
    hourstr=kt[0]
    minstr=kt[1]
    hr=int(hourstr)
    min=int(minstr)
    if(min<59):
        min=min+2
    else:
        min=2
        hr=hr+1
    print(hr)
    print(min)
    
    pwk.sendwhatmsg(mobilenumber,message,hr, min)
    
    
    pyautogui.click(1050, 950)
    
    
    time.sleep(15)
    k.press_and_release('enter')
    
