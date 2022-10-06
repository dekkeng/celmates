# Celmates Bot for cophead game
This is a cophead bot

# Requirements
- Installed Python 2.7+ (https://www.python.org/downloads/)
- OS: Windows 10 recommended

# How to run
1. Install Python if you don't already installed.
2. Clone the repository to a folder on your PC.
3. Open Powershell and go to the folder that you extracted from step 2
4. Run this command in Powershell to install required libraries
```bash
pip install -r requirements.txt
```
5. Change config.txt
6. Start the bot by double click at start.py or use command python start.py in Powershell (You need to open the game at maximized on this step).
7. If it not doing right, you need to adjust configurations in config.txt to fit your screen. (You need to change the values and try few times until it works) This should be one time work.
8. If you want to stop you just open something to hide the game screen and close your running script window.

# Configuration
There are default configurations that suit my screen, but you can adjust to suit your screen.
Adjust values inside config.txt file to suit your screen and run bot smoothly.

| Name | Description | Type | Default | Options |
| --- | --- | --- | --- | --- |
| HOLE_LEN_TO_JUMP | How far to jump if found hole | Pixel | 400 | |
| COKE_LEN_TO_JUMP | How far to jump if found coke | Pixel | 400 | |
| HOLE_JUMP_DURATION | How long to jump if found hole | Second | 1 | |
| COKE_JUMP_DURATION | How long to jump if found coke | Second | 0.1 | |
| BODY_LEFT_POSITION | x position of your player body on screen | Pixel | 889 | |

# Remarks
- This bot is created very quickly and might have some glitchs or bugs.

# Changelog
## v 0.0.1
+ Inital project
