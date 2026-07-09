import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from build.core import MusicPlayer

class App(ttk.Frame):
    def __init__(self, master, soundtrack_list: str):
        super().__init__(master)
        self.grid()

        self.COLORS = {
            "background": "#1C1C1C"
        }

        self.soundtrack_list = soundtrack_list

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
            relief="flat",
            padding=0
        )

        self.style.map(
            "Transparent.TButton",
            background=[("active", self.COLORS["background"]), ("pressed", self.COLORS["background"])]
        )
        
        self.actions = MusicPlayer(soundtrack_list)

        self.actual_title = tk.StringVar()
        self.actual_title.set("There is nothing to listen.")

        self.widgets(master)

            ###WIDGETS###

    def widgets(self, master):

        #adicionar o nome da pasta
        image_assets = {
            "next": "assets/forward.png",
            "prev": "assets/prev.png",
            "shuffle": "assets/shuffle.png",
            "play": "assets/play.png",
            "add_playlists": "assets/add_tracks.png"
        }
        self.valid_assets = {}
        for type, asset in image_assets.items():
            try:#nunca confie em arquivos e input de usúarios.
                img_pil = Image.open(asset).resize((32, 32), Image.Resampling.LANCZOS)#refaz o tamanho dos assets

                self.valid_assets[type] = ImageTk.PhotoImage(img_pil)
            except FileNotFoundError:
                print(f"Your file: {asset}. Could not be opened.")
                self.valid_assets[type] = None

        #onde é acionado a func retrogressing seu respectivo botao
        self.labels = ttk.Label(self,
                      textvariable=self.actual_title,
                      font=("Arial", 11, "bold"),
                      foreground="#FFFFFF",
                      background=self.COLORS["background"])
        self.labels.grid(row=2,column=1, columnspan=5)

        self.retrogress_song = ttk.Button(
            self,
            command=self.actions.retrogressing,
            image=self.valid_assets["prev"],
            style= "Transparent.TButton"
            )
        self.retrogress_song.grid(row=1,column=1)

        #Pause Button
        self.pause_button = ttk.Button(
            self,
            command= self.actions.pausing,
            image=self.valid_assets["play"],
            style= "Transparent.TButton"
            )
        self.pause_button.grid(row=1, column=2)

        #Pass button
        self.pass_song = ttk.Button(
            self,
            command=self.actions.passing,
              image=self.valid_assets["next"],
              style= "Transparent.TButton"
            )
        self.pass_song.grid(row=1,column=3)


        #Shuffle button
        self.random_track = ttk.Button(
            self,
            command=self.actions.shuffle,
            image=self.valid_assets["shuffle"],
            style= "Transparent.TButton"
            )
        self.random_track.grid(row=1, column=4)

        # Add track button
        self.add_tracks = ttk.Button(
            self,
            image=self.valid_assets["add_playlists"],
            style="Transparent.TButton")
        self.add_tracks.grid(row=1, column=5)

        self.windows_config(master)

#It sets configs for the root

    def windows_config(self, window):
        #cria e defina as proporcoes da janela,e seus aspectos.
        window.geometry("625x450")
        window.config(bg=self.COLORS["background"])
        window.title("Music Player by Yan")
        window.resizable(False, False) #Width, Height
        