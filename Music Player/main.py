import tkinter as tk

from gui.config import App

def main():
    root = tk.Tk()
    gui = App(root, "Laufeys_Songs")
    gui.mainloop()

if __name__ == "__main__":
    main()