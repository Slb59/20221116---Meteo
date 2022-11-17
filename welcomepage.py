from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import *
from PIL import ImageTk, Image

import tkinter as tk

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.id = controller.id

        self.create_widget()

    def create_widget(self):
        self.recherche_image = ImageTk.PhotoImage(Image.open('Images/recherche.jpg'))
        ril = tk.Label(master=self)
        ril.image = self.recherche_image
        ril.configure(image=self.recherche_image)
        ril.grid(row=0, column=0, pady=30)

        textfield = tk.Entry(self, justify="center", width=17, font=("poppins", 25, "bold"),
                             bg = "white", border=0, fg="black")
        textfield.grid(row=0, column=0)
        textfield.focus()

        self.loop_image = ImageTk.PhotoImage(Image.open('Images/loop.png'))
        recherche_button = tk.Button(self,
                                     image=self.loop_image,
                                     cursor="hand2",
                                     command=self.search_command(),
                                     border=0)
        recherche_button.configure(image=self.loop_image)
        recherche_button.place(x=390, y=52)

        self.logo_image = ImageTk.PhotoImage(Image.open('Images/Soleil.webp'))


    def search_command(self):
        pass


