import tkinter
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

##### Tkinter Config ######
root = customtkinter.CTk()
root.title('PyMusic')
root.geometry('400x480')
pygame.mixer.init()
##########################

list_of_songs = ['music/'] # Add more songs into this list, make sure they are .wav and put into the music Directory.
list_of_covers = ['img/'] # Add more JPEGS into the img directory, You can download city from my Github as a starting point.
n = 0

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4] 


    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)


def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.4)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progress)
    t1.start()


def skip_forward():
     play_music()

def skip_back():
    global n
    n -= 2
    play_music()

def volume(value):
    pygame.mixer.music.set_volume(value)


def selecionar_musica():
    arquivo = filedialog.askopenfilename(
        title="Selecionar música",
        filetypes=[("Arquivos de áudio", "*.mp3 *.wav *.ogg")]
    )

    if arquivo:
        pygame.mixer.music.load(arquivo)   
        pygame.mixer.music.play()       
        list_of_songs.configure(text=arquivo.split("/")[-1])



# All Buttons
skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

customtkinter.CTkButton(
    root,
    text="Abrir Música",
    command=selecionar_musica
).place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


root.mainloop()