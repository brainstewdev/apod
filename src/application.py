from tkinter.constants import ACTIVE, DISABLED, LEFT, NORMAL
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from nasa_api import nasa_api

class Application(tk.Frame):
    def change_img(self):
        self.img = PIL.ImageTk.PhotoImage(self.im)
        self.lab.config(image=self.img)
    def create_widget(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill='both', side='top')
        # create the get image button.
        tk.Button(master=self.button_frame,text="get image", command=self.open_image).pack(side=LEFT)
        # create the save image button (TO DO).
        self.save = tk.Button(master=self.button_frame,text="save image", state=DISABLED)
        self.save.pack(side= LEFT)
        # create the label which will be used to display the image
        self.lab = tk.Label(self)
        # pack the label
        self.lab.pack()
        # pack the window
        self.pack()
    def open_image(self):
        # get the image link from the api
        link = self.api.get_photo_link()
        # open the image using PIL.Image
        self.im = PIL.Image.open(self.api.get_stream_from_link(link=link))
        # display the image
        self.change_img()
        # enable the save button
        self.save["state"] = NORMAL
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        # initialise the nasa api object
        self.api = nasa_api()
        self.master = master
        # create all the widgets which will be used
        self.create_widget()
