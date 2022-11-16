from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import *

import tkinter as tk

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.id = controller.id

        recherche_image = PhotoImage('D:/coffre_1/Sylvie/Python/20221116---Meteo/Images/recherche.jfif')
        myimage = Label(image=recherche_image)
        myimage.place(x=20, y=20)

