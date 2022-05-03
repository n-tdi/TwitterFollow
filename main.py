from multiprocessing.connection import wait
from colorama import Fore
import ctypes, pyautogui, keyboard, os, time, random
from datetime import datetime

mainColor = Fore.LIGHTBLUE_EX

ascii_text = """
       ███╗░░██╗████████╗██████╗░██╗
       ████╗░██║╚══██╔══╝██╔══██╗██║
       ██╔██╗██║░░░██║░░░██║░░██║██║
       ██║╚████║░░░██║░░░██║░░██║██║
       ██║░╚███║░░░██║░░░██████╔╝██║
       ╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░╚═╝
"""

def sendCons(arg):
    print(f"\n       {Fore.WHITE}[{mainColor}Console{Fore.WHITE}] {arg}")

class Bot:
    def __init__(this):
        this.count = 0 # count for whatever it is you are doing

    def getPos(this): # get the position of the button
        sendCons("Move mouse to Following 1, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.buttonOne = pyautogui.position()
                break;
        time.sleep(0.5)
        sendCons("Move mouse to Following 2, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.buttonTwo = pyautogui.position()
                break;
        time.sleep(0.5)
        sendCons("Move mouse to Following 3, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.buttonThree = pyautogui.position()
                break;
        time.sleep(0.5)
        sendCons("Move mouse to Refresh button, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.buttonRefresh = pyautogui.position()
                break;
    
    def sendBot(this):
        pyautogui.moveTo(this.buttonOne) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.5)
        pyautogui.moveTo(this.buttonTwo) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.5)
        pyautogui.moveTo(this.buttonThree) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.5)
        pyautogui.moveTo(this.buttonRefresh) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.5)
        
        sendCons("One Cycle Follow Complete")
        this.count += 3 # add to count
        this.updateConsole() # update console

    def updateConsole(this): # update the console with stats
        os.system('cls') # clear screen
        this.updateTitle() # update title
        print(mainColor + ascii_text) # print ascii art
        sendCons("Starting bot loop") # start the loop of your main task
        sendCons("Hold G to quit") # if user wants to quit press g
        sendCons(f"Sent {this.count} follows") # print how many bots you sent
        now = time.time()
        elapsed = str(now - this.started_time).split(".")[0] # elapsed time
        sendCons(f"Elapsed time: {elapsed}s") # print how long you have been running

    def updateTitle(this):
        now = time.time()
        elapsed = str(now - this.started_time).split(".")[0] # elapsed time
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Bot | Sent Bots: {this.count} | Elapsed: {elapsed}s | Created by @professional-tdi on Github.")
    
    def main(this): # main function
        os.system('cls') # clear screen
        ctypes.windll.kernel32.SetConsoleTitleW("Bot | Created by @professional-tdi on Github.") # basic title with no info
        print(mainColor + ascii_text) # print ascii art
        this.getPos() # get position of button
        time.sleep(0.5)
        sendCons("Go to your twitter browseer window, then press G to start following") # go to proper window to click on
        while True:
            if keyboard.is_pressed('G'):
                break;
        os.system('cls') # clear screen again
        print(mainColor + ascii_text) # print ascii art again

        sendCons("Starting bot loop") # start the loop of your main task
        sendCons("Hold down G to quit") # if user wants to quit press g
        this.started_time = time.time() # setting started time
        time.sleep(0.5)
        while True:
            if keyboard.is_pressed('G'):
                break;
            this.sendBot() # send bot
            time.sleep(1) # wait 4 seconds
        sendCons(f"Finished following, followed {this.count} accounts") # finished botting

bot = Bot()
bot.main() # run main function
    

