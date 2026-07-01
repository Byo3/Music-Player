import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from build.core import MusicPlayer

class App(ttk.Frame):
    def __init__(self, master, soundtrack_list: list):
        super().__init__(master)
        self.grid()

        self.COLORS = {
            "background": "#1C1C1C"
        }


        #Config for widgets and the frame

        self.style = ttk.Style()
        
        self.style.configure(
            "Tframe",
            background=self.COLORS["background"]
        )

        self.style.configure(
            "Transparent.TButton",
            background=self.COLORS["background"],
            borderwidth=0,
            relief="flat"
        )

        self.style.map(
            "Transparent.TButton",
            background=[("active", self.COLORS["background"]), ("pressed", self.COLORS["background"])]
        )
        
        self.actions = MusicPlayer(soundtrack_list)
        self.widgets(master)

    def widgets(self, master):

        #adicionar o nome da pasta
        image_assets = {
            "next": "assets/forward.png",
            "prev": "assets/rewind.png",
            "shuffle": "assets/musica.png",
            "play": "assets/play.png"
        }
        self.valid_assets = {}
        for type, asset in image_assets.items():
            try:#nunca confie em arquivos e input de usúarios.
                img_pil = Image.open(asset)
                self.valid_assets[type] = ImageTk.PhotoImage(img_pil)
            except FileNotFoundError:
                print(f"Your file: {asset}. Could not be opened.")
                self.valid_assets[type] = None

        #onde é acionado a func retrogressing seu respectivo botao
        self.retrogress_song = ttk.Button(
            self,
            command=self.actions.retrogressing,
            text="Prev",
            image=self.valid_assets["prev"],
            style= "Transparent.TButton"
            )
        self.retrogress_song.grid(row=3,column=1)

        #Pause Button
        self.pause_button = ttk.Button(
            self,
            command= self.actions.pausing,
            text="Pause",
            image=self.valid_assets["play"],
            style= "Transparent.TButton"
            )
        self.pause_button.grid(row=3, column=2)

        #Pass button
        self.pass_song = ttk.Button(
            self,
            command=self.actions.passing,
              text="Next",
              image=self.valid_assets["next"],
              style= "Transparent.TButton"
            )
        self.pass_song.grid(row=3,column=3)


        #Shuffle button
        self.random_track = ttk.Button(
            self,
            command=self.actions.shuffle,
            text="random",
            image=self.valid_assets["shuffle"],
            style= "Transparent.TButton"
            )
        self.random_track.grid(row=3,column=4)

        self.windows_config(master)


    def windows_config(self, window):
        #cria e defina as proporcoes da janela,e seus aspectos.
        window.geometry("500x450")
        window.config(bg=self.COLORS["background"])
        window.title("Music Player by Yan")
        window.resizable(False, False) #Width, Height
