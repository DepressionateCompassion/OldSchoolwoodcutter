#import pyautogui and time so that we can make use of their features.
import pyautogui
import time
#defining droppinglogs when our inventory is full and if it is not, it will just print out inventory is not full.
def droppinglogs():
    logs = pyautogui.locateOnScreen('Logs2.JPG',confidence=0.9)
    if logs != None:
        for x in range (0,27):
            logs2 = pyautogui.locateOnScreen('Logs1.JPG',confidence=0.9)
            logcenter = pyautogui.center(logs2)
            logsX , logsY = logcenter
            pyautogui.moveTo(logsX,logsY,0.25)
            pyautogui.keyDown('shift')
            pyautogui.click()
            pyautogui.keyUp('shift')
    if logs == None:
        print("Inventory Not Full")

#The main function that will combine locating tree, clicking on tree to cut down the tree and dropping logs if inventory is full.
#This makes use of pyautoguiclick, pyautogui.moveto,pyautogui.locateOnScreen and time.sleep and the if functions and while function of python.

while True:
    time.sleep(3)
    Tree = pyautogui.locateOnScreen('Tree1.jpg',confidence=0.55)
    if Tree != None:
        Treecenter =pyautogui.center(Tree)
        TreeX, TreeY = Treecenter
        pyautogui.moveTo(TreeX,TreeY,0.75)
        pyautogui.click()
        deadlog = pyautogui.locateOnScreen('Deadlog.JPG',confidence=0.5)
        if deadlog != None:
            continue
        elif deadlog == None:
            time.sleep(deadlog!=None)
    elif Tree == None:
        Tree = pyautogui.locateOnScreen('Tree2.JPG',confidence=0.55)
        if Tree != None:
            Treecenter = pyautogui.center(Tree)
            TreeX, TreeY = Treecenter
            pyautogui.moveTo(TreeX,TreeY,0.75)
            pyautogui.click()
            deadlog = pyautogui.locateOnScreen('Deadlog.JPG',confidence=0.5)
            if deadlog != None:
                continue
            elif deadlog == None:
                time.sleep(deadlog!=None)
        elif Tree == None:
            Tree = pyautogui.locateOnScreen('tree3.JPG',confidence=0.55)
            if Tree != None:
                Treecenter = pyautogui.center(Tree)
                TreeX, TreeY = Treecenter
                pyautogui.moveTo(TreeX,TreeY,0.75)
                pyautogui.click()
                deadlog = pyautogui.locateOnScreen('Deadlog.JPG',confidence=0.5)
                if deadlog != None:
                    continue
                elif deadlog == None:
                    time.sleep(deadlog!=None)
                print(Tree)
                
            elif Tree == None:
                Tree = pyautogui.locateOnScreen('tree4.JPG',confidence=0.55)
                if Tree != None:
                    Treecenter = pyautogui.center(Tree)
                    TreeX, TreeY = Treecenter
                    pyautogui.moveTo(TreeX,TreeY,0.75)
                    pyautogui.click()
                    print(Tree)
                    deadlog = pyautogui.locateOnScreen('Deadlog.JPG',confidence=0.5)
                    if deadlog != None:
                            continue
                    elif deadlog == None:
                        time.sleep(deadlog!=None)
                else: 
                    print(Tree)
    droppinglogs()
