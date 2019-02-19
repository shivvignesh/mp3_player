import os
import pygame
from mutagen.id3 import ID3
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

root=Tk()
root.minsize(400,400)

listofsongs=[]
new_list=[]

index=0

listbox=Listbox(root)
listbox.pack()


def directorychooser():
	directory=filedialog.askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith('.mp3'):
			listofsongs.append(files)
			#print(files)
	#print(listofsongs)
	#listofsongs.reverse()
	#print(new_list)
	
def play():

	song=listbox.curselection()
	#print(song)
	song_no=song[0]

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[song_no])
	pygame.mixer.music.play()

	print(song,listofsongs)

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

vol=0.0

def volume_up():
	global vol

	pygame.mixer.init()
	vol=vol+0.2
	pygame.mixer.music.set_volume(vol)

def volume_down():
	global vol

	pygame.mixer.init()
	vol=vol-0.2
	pygame.mixer.music.set_volume(vol)


directorychooser()



for items in listofsongs:
	listbox.insert(END,items)

play_button=Button(root,text="Play",command=play)
play_button.pack()

stop_button=Button(root,text="Stop",command=stop)
stop_button.pack()

pause_button=Button(root,text="pause",command=pause)
pause_button.pack()

volume_up_button=Button(root,text="volume up",command=volume_up)
volume_up_button.pack()

volume_down_button=Button(root,text="volume down",command=volume_down)
volume_down_button.pack()


root.mainloop()