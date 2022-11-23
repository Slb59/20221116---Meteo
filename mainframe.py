import tkinter as tk

from tkinter import font as tkfont
from welcomepage import WelcomePage
from citypage import CityPage

from meteodata import MeteoData

class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family="Verdana", size=12, weight="bold", slant='roman')
        self.title("Application Météo")
        self.geometry("900x500+300+200")
        self.resizable(False, False)

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nesw')

        self.id = tk.StringVar()
        self.id.set('Mister smith')

        self.listening = {}

        self.cities = ['Montalivet', 'Méjannes-le-Clap', 'Cantin', 'Feignies', 'Narbonne']
        self.citiesdata = {}
        self.load_data()

        self.current_city = self.cities[0]

        page_name = WelcomePage.__name__
        frame = WelcomePage(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky='nesw')
        self.listening[page_name] = frame

        for c in self.cities:
            self.current_city = c
            page_name = c
            frame = CityPage(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky='nesw')
            self.listening[page_name] = frame

        self.up_frame('WelcomePage')

    def up_frame(self, page_name):
        page = self.listening[page_name]
        page.tkraise()

    def load_data(self):
        for c in self.cities:
            meteodata = MeteoData(c)
            self.citiesdata[c] = meteodata


