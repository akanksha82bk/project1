from tkinter import *
from tkinter import filedialog
import tkinter
import tkinter.font
import tkinter as tk
import pygame
pygame.init()
 
class musicplay:
 def __init__(self):
   self.music = None
   self.play_list = []
   self.trackLocations = []
   self.root = tk.Tk()
   self.ispaused = False
   self.root.title("adaaPlayer")
   self.root.configure(background='black')
   self.root.geometry('300x100+750+300')
   self.filename = tkinter.StringVar()
   self.name = tkinter.StringVar()
   self.play_list = tkinter.StringVar()
   self.buffer = list()
   menubar = Menu(self.root)
   filemenu = Menu(menubar, tearoff=0, bg="black", fg="Orange")
   menubar.add_cascade(label='File', menu = filemenu)
   filemenu.add_command(label='Open', command = self.open_file)
   filemenu.add_separator()
   filemenu.add_command(label='Exit', command = self.Exit)
   self.root.config(menu=menubar)
 
   save_button = Button(self.root, width = 6, height = 1,
   text = 'save',fg='Orange',command = self.saveInFile, bg='black')
   save_button.grid(row=0, column=3)
 
   play_button = Button(self.root, width = 5, height = 1, text='Play',
   fg='Orange', command = self.play, bg="black")
   play_button.grid(row=0, column=0, sticky = W)
 
   stop_button = Button(self.root, width = 5, height = 1, text='Stop',
   fg='Orange', command = self.stop, bg="black")
   stop_button.grid(row=0, column=1, sticky = W)
 
   pause_button = Button(self.root, width = 5, height = 1, text='Pause',
   fg='Orange', command = self.pause, bg="black")
   pause_button.grid(row=0, column=2)
 
   self.volume_slider = Scale(self.root, label='Volume',
   orient = 'horizontal', fg = 'Orange', 
   command = self.vol, bg="black")
   self.volume_slider.grid(row=0, column=4)
 
   file_name_label = Label(self.root, font=('Comic Sans', 8),
   fg = 'Orange', wraplength = 300,
   textvariable=self.name, bg="black")
   file_name_label.grid(row=3, column=0, columnspan=8)
 
   play_list_window = Toplevel(self.root, height = 200, width = 100)
   play_list_window.title("myPlaylist")
   self.play_list_display = Listbox(play_list_window, selectmode=EXTENDED,
   width = 50, bg="Dark Slate grey",
   fg="Orange")
   self.play_list_display.bind("<Double-Button-1>", self.tune_changed)
   self.play_list_display.pack()
   play_list_window.mainloop()
 
   self.root.mainloop() 
 
 def open_file(self): 
  self.filename.set(tkinter.filedialog.askopenfilename(defaultextension = ".mp3",
                                                       filetypes=[ ("All Types", "*.*"), ("MP3", "*.mp3")]))
  self.playlist = self.filename.get()
  self.buffer.append(self.playlist)
  playlist_pieces = self.playlist.split("/")
  self.play_list.set (playlist_pieces[-1])
  playl = self.play_list.get()
  self.play_list_display.insert(END, playl)
  print( self.filename.get())
  pygame.mixer.music.load(self.filename.get())

  pieces = self.filename.get().split("/")
  self.trackLocations += [self.filename.get()]
  self.name.set(pieces[-1])
 
 def play(self):
     pygame.mixer.music.play() 
     #self.play
 def stop(self):
   pygame.mixer.music.stop()
   #self.stop
 def pause(self):
  
  if  self.ispaused :
       pygame.mixer.music.unpause()
       self.ispaused = False
  else:
       pygame.mixer.music.pause()
       self.ispaused = True
       
 
 def vol(self, event):
  v = Scale.get(self.volume_slider)
  try:
   pygame.mixer.music.set_volume(v)
  except:
   pass
 
 def tune_changed(self, event):
  idx = event.widget.curselection()[0]
  pygame.mixer.music.load(self.trackLocations[int(idx)])
  print ("Now playing %s" % event.widget.get(idx))
 def saveInFile(self):
     data ="\n".join(self.buffer)
     ptr = open("playlist.txt","a")
     ptr.write(data)
     ptr.close()
     
 
 def Exit(self):
  exit()
 
if __name__ == "__main__":
  musicplay()
