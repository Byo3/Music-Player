import random 
import tkinter
from tkinter import ttk


messages_error = {
    "impossible_range": "You have reached of the begining of you playlist.",
    "end_range": "There is no music. Add more?"
}

class MusicPlayer():
    def __init__(self, song_list: list):
        self.song_list = song_list
        self.ERRORS = messages_error
        self.is_playing = True
        self.index = 0

    def passing(self):
        if self.index > (len(self.song_list) - 1):
            raise ValueError(self.ERRORS["end_range"])
    
        self.index += 1
        print(self.song_list[self.index])

    def retrogressing(self):
        if self.index <= 0:
            raise ValueError(self.ERRORS["impossible_range"])

        self.index -= 1
        print(self.song_list[self.index])

    def shuffle(self):
        random.shuffle(self.song_list)
        self.index = 0
        print(self.song_list[self.index])

    def pausing(self):
        self.is_playing = not self.is_playing
        print("Pausado" if not self.is_playing else "Despausado")
