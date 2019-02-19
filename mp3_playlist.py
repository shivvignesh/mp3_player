import os
import pygame
from mutagen.id3 import ID3
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

root=Tk()
root.minsize(400,400)

listofsongs=[]

index=0

def directorychooser():
	directory=filedialog.askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith('.mp3'):
			listofsongs.append(files)

	
def play():
	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[1])
	pygame.mixer.music.play()

def stop():
	pygame.mixer.init()
	pygame.mixer.music.stop()

count=0

def pause():
	global count

	if count==0:
		pygame.mixer.init()
		pygame.mixer.music.pause()
		count=1
	else:
		pygame.mixer.init()
		pygame.mixer.music.unpause()
		count=0


directorychooser()


listbox=Listbox(root)
listbox.pack()

for items in listofsongs:
	listbox.insert(0,items)

play_button=Button(root,text="Play",command=play)
play_button.pack()

stop_button=Button(root,text="Stop",command=stop)
stop_button.pack()

pause_button=Button(root,text="pause",command=pause)
pause_button.pack()

root.mainloop()