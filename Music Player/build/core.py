#Buscar se há um possibilidade de fazer o user ao baixar
#instalar os pacotes necessários. Sendo eles:
#python 
#PIL -> pillow
#C++
#pyland11
#vlc
#tinytag

import random 
import vlc
from tinytag import TinyTag
import os


class MusicPlayer():
    def __init__(self, folder: str):
        self.folder = folder
        self.is_playing = False
        self.index = 0

        self.play = None
        self.playlist = self.def_info(self.folder)
        
        self.play = vlc.MediaPlayer(self.playlist[self.index])


    def def_info(self, usr_folder: str):

        if not usr_folder:
            print("Your foulder is empty. Add tracks.")

        try:
            arquivos = os.listdir(usr_folder)
            file_list =[]

            for files in arquivos:
                if files.endswith("mp3"):
                    file_list.append(os.path.join(usr_folder, files))

            return file_list
        
        except FileNotFoundError:
            print(f"file: {usr_folder} had not found")
            return []

    def passing(self):
        if self.index >= (len(self.playlist) - 1):
            self.index = (self.index + 1) % len(self.playlist)

        else:
            self.index += 1
        
        if self.play is not None:
            self.play.stop()

        new_media = vlc.Media(self.playlist[self.index])
        self.play.set_media(new_media)# type: ignore
        self.play.play()# type: ignore

        print(self.playlist[self.index])

    def retrogressing(self):
        if self.index <= 0:
            raise ValueError("You are at the begining of the you playlist")
        
        else:
            self.index -= 1
        
        if self.play is not None:
            self.play.stop()

        new_media = vlc.Media(self.playlist[self.index])
        self.play.set_media(new_media)# type: ignore
        self.play.play()# type: ignore

        print(self.playlist[self.index])

    def shuffle(self):
        random.shuffle(self.playlist)

        if self.play is not None:
            self.play.stop()

        self.index = 0

        new_media = vlc.Media(self.playlist[self.index])
        self.play.set_media(new_media)# type: ignore
        self.play.play()# type: ignore

        print(self.playlist[self.index])

    def pausing(self) -> None:
        if self.play is None:
            self.play = vlc.MediaPlayer(self.playlist[self.index])

        self.is_playing = not self.is_playing

        if self.is_playing:
           self.play.play() #type: ignore   
           print(f"Playing: {self.playlist[self.index]}")
        else:
            self.play.pause()# type: ignore
            print(f"Paused: {self.playlist[self.index]}")

#fazer que a lista de musica se tranforme e um dicionários das músicas,
#separando-o com sua respectiva informaçao.