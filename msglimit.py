import time
import pyautogui as p
import pywhatkit as wp

wp.sendwhatmsg("+919048964884", "<3", 15, 54)

for i in range(100):
    p.typewrite("KARMA exist ... ! " + str(i))
    p.press("<3")
