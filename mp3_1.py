import os
import pygame
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

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[1])
	pygame.mixer.music.play()

directorychooser()



root.mainloop()