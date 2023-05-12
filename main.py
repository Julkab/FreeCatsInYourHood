from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from typing import Self
# pip3 install customtkinter
import customtkinter
from finder import finder

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    city = None
    def __init__(self):
        super().__init__()
        self.geometry("350x200")
        self.title("Free Cats In Your Hood")

        self.button = customtkinter.CTkButton(self, text="Yes", command = self.yes)
        self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.N)   #like NESW 

        self.qwery1 = customtkinter.CTkLabel(self, text="Will you be a good cat owner?:")
        self.qwery1.place(relx=0.5, rely=0.5, anchor=customtkinter.S)


    def yes(self):
        dialog = customtkinter.CTkInputDialog(text="Enter the city you live:", title="Free Cats In Your Hood")
        self.city = dialog.get_input()
        finder_object = finder(self.city)
        finder_object.scraping()
        
customtkinter.set_appearance_mode("system")
app = App()
app.mainloop()