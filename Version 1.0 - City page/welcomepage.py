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

        self.nomville = tk.Label(master=self, font=('arial', 15, 'bold'), text='nom')
        self.nomville.grid(row=2, column=0)

        self.textfield = tk.Entry(self, justify="center", width=17, font=("poppins", 25, "bold"),
                             bg = "white", border=0, fg="black")
        self.textfield.grid(row=0, column=1)
        self.textfield.insert(END, 'Paris')
        self.textfield.focus()

        self.loop_image = ImageTk.PhotoImage(Image.open('Images/loop.png'))
        recherche_button = tk.Button(master=self,
                                     cursor="hand2",
                                     command=lambda: self.meteo_data(),
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
        label2.place(x=150, y=365)

        label3 = tk.Label(master=self, text='DESCRIPTION', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label3.place(x=270, y=365)

        label4 = tk.Label(master=self, text='PRESSION', font=('Helvetica', 15, 'bold'),
                          fg='white', bg='#1ab5ef')
        label4.place(x=600, y=365)

        self.t = tk.Label(master=self,
                     font=('arial', 50, "bold"),
                     bg='#ee666d')
        self.t.grid(row=2, column=1, pady=5)

        self.c = tk.Label(master=self,
                     font=('arial', 15, "bold"),
                     bg='#ee666d'
                     )
        self.c.grid(row=3, column=1, pady=5)

        self.v = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        self.v.place(x=70, y=430)

        self.h = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        self.h.place(x=150, y=430)

        self.d = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        self.d.place(x=270, y=430)

        self.p = tk.Label(master=self,
                     text='...',
                     font=('arial', 20, 'bold'),
                     bg='#1ab5ef')
        self.p.place(x=600, y=430)

        self.heure = tk.Label(master=self, font=('Helvetica', 20), text='heure')
        self.heure.grid(row=3, column=0)

    def meteo_data(self):
        try:
            city = self.textfield.get()
            geolocalisation = Nominatim(user_agent="geoapiExercices")
            location = geolocalisation.geocode(city)
            obj = TimezoneFinder()
            resultat = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(resultat)
            locat_time = datetime.now(home)
            heure_actuel = locat_time.strftime("%H:%M:%S")
            self.heure.config(text=heure_actuel)
            self.nomville.config(text='Météo actuelle')

            apicle  = "96e5845ca3da53f5a1f19e2b3a15157f"

            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apicle+"&lang=fr"

            json_data = requests.get(api).json()
            description = json_data["weather"][0]["description"]
            temp = int(json_data["main"]["temp"]-273.15)
            pression = json_data["main"]["pressure"]
            humidity = json_data["main"]["humidity"]
            vent = json_data["wind"]["speed"]

            self.t.config(text=(temp, "°"))
            self.v.config(text=vent)
            self.h.config(text=humidity)
            self.d.config(text=description)
            self.p.config(text=pression)

        except Exception as e:
            messagebox.showerror("Application météo", "Invalide")
            print(e)


