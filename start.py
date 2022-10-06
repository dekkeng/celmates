from time import sleep
from player import Player


sleep(2)
print("Start Celmates Bot!")
player = Player()

try:
    while True:
        player.loop()
except Exception as e:
    player.log(e)
    pass