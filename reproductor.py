#Maria Jennifer Carbajal Martinez 41s
#1 REPRODUCTOR
from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init() #iniciamos modulo pygame

#funcion boton abrir cancion
def openFileSong():
    cancion = filedialog.askopenfilename()  #guardar el nombre o cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
        
    
def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()
    
def pauseSong():
    pygame.mixer.music.pause()
    
def volumenUp():
    levelup=pygame.mixer.music.get_volume() +0.1
    print(levelup)
    pygame.mixer.music.set_volume(levelup)

def volumenDown():
    leveldown=pygame.mixer.music.get_volume() -0.1
    print(leveldown)
    pygame.mixer.music.set_volume(leveldown)

raiz = Tk()
raiz.title("Reproductor MP3 - GUI")
#raiz.iconbitmap("disk-jockey.ico")
raiz.geometry("900x300")
raiz.resizable(0,0)

#Crear frame
framePrincipal = Frame(raiz, bg="#4a4a4a")
framePrincipal.pack(fill="both", expand=1)

#TITULO DEL REPRODUCTOR
tituloReproductor = Label(framePrincipal, text="Reproductor mp3", font=("Vanilla Caramel", 20, "bold"), bg="#4a4a4a", fg="#fbfbfb")
tituloReproductor.place(relx=0.35,rely=0.1)

#botton open song
botonOpenSong = Button(framePrincipal, text="Open Song", bg="#0099FF", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=openFileSong)
botonOpenSong.place(relx=0.01, rely=0.3)

#Play song
botonPlaySong = Button(framePrincipal, text="Play song", bg="#9900FF", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=playSong) #e2504c rojo, #42ab49 verde, #ffc400 amarillo, #55009 morado, #0000FF
botonPlaySong.place(relx= 0.22, rely=0.3)

#Stop song 
botonStopSong = Button(framePrincipal, text="Stop song", bg="#ffc400", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=stopSong)
botonStopSong.place(relx= 0.44, rely=0.3)

#Resume
botonResumeSong = Button(framePrincipal, text="ResumeSong", bg="#9900FF", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=resumeSong)
botonResumeSong.place(relx= 0.66, rely=0.3)

#Pause
botonPause = Button(framePrincipal, text="Pause", bg="#0099FF", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=pauseSong)
botonPause.place(relx= 0.87, rely=0.3)

#Volumenmas
botonVolumenUp = Button(framePrincipal, text="Volumen +", bg="#CC0033", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenUp)
botonVolumenUp.place(relx= 0.22, rely=0.65)

#Volumenmenos
botonVolumenDown = Button(framePrincipal, text="Volumen -", bg="#CC0033", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenDown)
botonVolumenDown.place(relx= 0.66, rely=0.65)

raiz.mainloop()