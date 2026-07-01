import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from gui.config import App
playlist = [
    {"song": "Godness", "artist": "Laufey"},
    {"song": "See you again", "artist": "Tyler the Creator"},
    {"song": "二時間だけのバカンス", "artist": "Sheena Ringo"}]
#Aqui ficará alocado as informacoes seja elas: artista e nome da cançao. Ainda
#nao foi acabado.

def main():
    root = tk.Tk()
    gui = App(root, playlist)
    gui.mainloop()


if __name__ == "__main__":
    main()