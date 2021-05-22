# status_1
# Author : MrRobot
# requirement library
from pytube import YouTube
from pytube.cli import on_progress
import time
import sys,os


# Banners
print('''
__   __ _____ ______         ______  _     
\ \ / /|_   _|| ___ \        |  _  \| |    
 \ V /   | |  | |_/ / ______ | | | || |    
  \ /    | |  | ___ \|______|| | | || |    
  | |    | |  | |_/ /        | |/ / | |____
  \_/    \_/  \____/         |___/  \_____/
                                           
''' )
bannerChoosen = '''	
  [ 1 ] Video.
  [ 2 ] Audio.
  [ 99 ] Exit.

'''
bannerVideo = '''

 _   _  _      _              
| | | |(_)    | |             
| | | | _   __| |  ___   ___  
| | | || | / _` | / _ \ / _ \ 
\ \_/ /| || (_| ||  __/| (_) |
 \___/ |_| \__,_| \___| \___/ 
                              
                              
'''
bannerAudio = '''

  ___              _  _        
 / _ \            | |(_)       
/ /_\ \ _   _   __| | _   ___  
|  _  || | | | / _` || | / _ \ 
| | | || |_| || (_| || || (_) |
\_| |_/ \__,_| \__,_||_| \___/ 
                               
                               
'''


# MainMenu
print(bannerChoosen)

def ytb_vid():
    # clear screen
    os.system('clear')
    print(bannerVideo)
    # get url link
    url = input("Enter video url : ")
    yt = YouTube(url,on_progress_callback=on_progress)
    # user that the process has started
    yt = yt.streams[0].download('Downloads')
    # download progress
    print ("\n[                    ] 0% ")
    time.sleep(5)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(5)
    print("[===============     ] 75%")
    time.sleep(5)
    print("[====================] 100%")
    time.sleep(3)
    # Download complited.
    print("\nDownloaded successfully!")
    time.sleep(5)
    sys.exit()
    
    ytb_vid()

def ytb_mp3():
    # clear screen
    os.system('clear')
    print(bannerAudio)
    # get url link
    yt = YouTube(input("Enter video url : "))
    # accessing audio streams of YouTube obj.(first one, more available)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    # download progress
    print ("\n[                    ] 0% ")
    time.sleep(5)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(5)
    print("[===============     ] 75%")
    time.sleep(5)
    print("[====================] 100%")
    time.sleep(3)
    # Download complited.
    print("\nDownloaded successfully!")
    time.sleep(5)
    sys.exit()
    
    ytb_mp3()
    
int = [1, 2, 99]
    
menu_choosen = input(" ~#  ")
if menu_choosen=="1":
	ytb_vid()
elif menu_choosen == "2":		
	ytb_mp3()
elif menu_choosen == "99":
	print("\n@MrRobot, GoodBye ;)")
	os.system('exit')
	sys.exit()
else:
	print("ERROR, Choosen invaild!")

# status_0
