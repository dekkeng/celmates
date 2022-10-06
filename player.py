import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from random import uniform

load_dotenv("config.txt")

class Player:
    def __init__(self):
        self.HOLE_LEN_TO_JUMP = float(os.getenv('HOLE_LEN_TO_JUMP', 30))
        self.COKE_LEN_TO_JUMP = float(os.getenv('COKE_LEN_TO_JUMP', 50))
        self.HOLE_JUMP_DURATION = float(os.getenv('HOLE_JUMP_DURATION', 0.1))
        self.COKE_JUMP_DURATION = float(os.getenv('COKE_JUMP_DURATION', 0.01))
        self.BODY_LEFT_POSITION = float(os.getenv('BODY_LEFT_POSITION', 889))
        self.updatePos()

    def loop(self):
        self.updatePos()
        if self.retry == None:
            if self.hole != None and len(self.hole) != 0:
                self.hole.sort(key=lambda w: w[0], reverse = True)
                if -20 < (self.hole[0][0] - self.BODY_LEFT_POSITION) < self.HOLE_LEN_TO_JUMP:
                    self.jump(self.HOLE_JUMP_DURATION)
            if self.coke != None and len(self.coke) != 0:
                self.coke.sort(key=lambda w: w[0], reverse = True)
                if -20 < (self.hole[0][0] - self.BODY_LEFT_POSITION) < self.COKE_LEN_TO_JUMP:
                    self.jump(self.COKE_JUMP_DURATION)

    def updatePos(self):
        self.coke = list(self.getAllPos("coke"))
        self.hole = list(self.getAllPos("hole"))
        self.retry = self.getPos("retry")
    
    def jump(self, conf = 0.1):
        self.log("JUMP")
        pyautogui.keyDown("space")
        self.wait(conf)
        pyautogui.keyUp("space")

    def getPos(self, file, conf = 0.75):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf)

    def getAllPos(self, file, conf = 0.75):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf)

    def wait(self, length = 0.01):
        sleep(length)

    def move(self, pos):
        pyautogui.moveTo(pos)
        
    def click(self, pos):
        pyautogui.click([uniform(pos[0], pos[0]+self.RANDOM_CLICK_SIZE), uniform(pos[1], pos[1]+self.RANDOM_CLICK_SIZE)])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')
