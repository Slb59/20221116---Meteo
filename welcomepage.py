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

        recherche_image = ImageTk.PhotoImage(Image.open('Images/recherche.jpg'))
        ril = tk.Label(master=self)
        ril.image = recherche_image
        ril.configure(image=recherche_image)
        ril.grid(row=0, column=0, pady=30)


