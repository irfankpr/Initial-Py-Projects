import time
import pyautogui as p

time.sleep(5)
for i in range(1000):
    p.typewrite("nirthada PUBG : "+str(i))
    p.press("enter")
