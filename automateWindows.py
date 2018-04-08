import pyautogui
from time import sleep
pyautogui.FAILSAFE = False

class browser(object):
   def __init__(self,browser):
       self.browser = browser

   def openBrowser(self):
       pyautogui.press("win")
       pyautogui.typewrite(self.browser)
       pyautogui.press("enter")

   def openSite(self,websites):
        for website in websites:
            if website == websites[0]:
                sleep(2)
                pyautogui.hotkey("ctrl", "e")
                pyautogui.press("backspace", 2)
                pyautogui.typewrite(website)
                pyautogui.press("enter")
            else:
                self.newTab(website)

   def newTab(self,website):
       sleep(2)
       pyautogui.hotkey("ctrl", "t")
       sleep(0.2)
       pyautogui.typewrite(website)
       pyautogui.press("enter")

def typeSomething(message):
    pyautogui.typewrite(message)

def openProgram(program):
    sleep(2)
    pyautogui.hotkey("win", "d")
    pyautogui.press("win")
    pyautogui.typewrite(program)
    pyautogui.press("enter")

def mood_select():
    print ("    What mood are you in today?")
    mood = input("""
        Networking  1
        Gaming      2
        Youtube     3
        Netflix     4

    """)
    edge = browser("Edge")
    edge.openBrowser()
    if int(mood) == 1:
        websites = ["www.packetpushers.net", "www.reddit.com/r/networking"]
        edge.openSite(websites)
        openProgram("GNS3")
    if int(mood) == 2:
        websites = ["gaming.youtube.com", "www.reddit.com/r/gaming"]
        edge.openSite(websites)
        openProgram("Steam")
    if int(mood) == 3:
        websites = ["www.youtube.com/tv"]
        edge.openSite(websites)
    if int(mood) == 4:
        websites = ["www.netflix.com"]
        edge.openSite(websites)

mood_select()
