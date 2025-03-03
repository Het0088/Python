from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def whatsapp(name,msg):
    
    # startfile("")
    
    sleep(15)
    click(x=254, y=118)
    sleep(1)
    write(name)
    
