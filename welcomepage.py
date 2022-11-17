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
        rechImg = Image.open('Images/recherche.jpg')
        rechImg = rechImg.resize((550, 102))

        self.recherche_image = ImageTk.PhotoImage(rechImg)
        ril = tk.Label(master=self)
        ril.image = self.recherche_image
        ril.configure(image=self.recherche_image)
        ril.grid(row=0, column=1, pady=30)

        textfield = tk.Entry(self, justify="center", width=17, font=("poppins", 25, "bold"),
                             bg = "white", border=0, fg="black")
        textfield.grid(row=0, column=1)
        textfield.focus()

        self.loop_image = ImageTk.PhotoImage(Image.open('Images/loop.png'))
        recherche_button = tk.Button(self,
                                     image=self.loop_image,
                                     cursor="hand2",
                                     command=self.search_command(),
                                     border=0)
        recherche_button.configure(image=self.loop_image)
        recherche_button.place(x=720, y=52)

        image = Image.open('Images/Soleil.jpg')
        image = image.resize((150, 150))
        self.logo_image = ImageTk.PhotoImage(image)

        logofield = tk.Label(master=self, border=0)
        logofield.image = self.logo_image
        logofield.configure(image=self.logo_image)
        logofield.grid(row=0, column=0, sticky='w')

        fondImg = Image.open('Images/fond.jpg')
        print(fondImg.size)
        fondImg = fondImg.resize((850,200))
        self.fond_image = ImageTk.PhotoImage(fondImg)
        fondfield = tk.Label(master=self, border=0)
        fondfield.image = self.fond_image
        fondfield.configure(image=self.fond_image)
        fondfield.grid(row=4, columnspan=2, pady=20)

        label1 = tk.Label(master=self, text='VENT', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label1.place(x=70, y=365)

        label2 = tk.Label(master=self, text='HUMIDITE', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label2.place(x=200, y=365)

        label3 = tk.Label(master=self, text='DESCRIPTION', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label3.place(x=350, y=365)

        label4 = tk.Label(master=self, text='PRESSION', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label4.place(x=560, y=365)

        t = tk.Label(master=self,
                     font=('arial', 50, "bold"),
                     bg='#ee666d')
        t.grid(row=2, column=1, pady=5)

        c = tk.Label(master=self,
                     font=('arial', 15, "bold"),
                     bg='#ee666d'
                     )
        c.grid(row=3, column=1, pady=5)

        v = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        v.place(x=70, y=430)

        h = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        h.place(x=200, y=430)

        d = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        d.place(x=350, y=430)

        p = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        p.place(x=560, y=430)


    def search_command(self):
        pass


