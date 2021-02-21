from tkinter.constants import DISABLED, LEFT, NORMAL, YES
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import tkinter as tk
from nasa_api import nasa_api

class Application(tk.Frame):
    # event called when the window is resized
    def _resize(self, event):
        if event == tk.EventType.ResizeRequest:
            self._resize_img(event.width, event.height)
    def _resize_img(self, width, height):
        # self.im = self.im.resize((width, height))
        self.im = PIL.ImageOps.fit(self.original_image, (width, height))

        self.change_img()
    def change_img(self):
        # create a PhotoImage obj from the im returned by the api
        self.img = PIL.ImageTk.PhotoImage(self.im)
        # set the label image value to the image i got 
        self.lab.config(image=self.img)
    # function used to create all of the widgets used
    def create_widget(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill='both', side='top')
        # create the get image button.
        tk.Button(master=self.button_frame,text="get image", command=self.open_image).pack(side=LEFT)
        # create the save image button (TO DO).
        self.save = tk.Button(master=self.button_frame,text="save image", command=self.save_image, state=DISABLED)
        self.save.pack(side= LEFT)
        # create the label which will be used to display the image
        self.lab = tk.Label(self)
        # pack the label
        self.lab.pack(expand=YES)
        # pack the window
        self.pack()
    def save_image(self):
        # get the photo title from the api
        fname = str(self.api.get_photo_title())
        # get the string to be a valid filename (as seen in this answer: https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename#comment25028115_295152)
        fname = "".join(i for i in fname if i not in "\/:*?<>|")
        # save the image
        self.im.save(f"images\\{fname}.jpg")
    def open_image(self):
        # get the image link from the api
        link = self.api.get_photo_link()
        # open the image using PIL.Image
        self.original_image = PIL.Image.open(self.api.get_stream_from_link(link=link))
        self.im = self.original_image
        self.im_name = self.api.get_photo_title()
        # display the image
        self.change_img()
        # enable the save button
        self.save["state"] = NORMAL
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        master.title("APOC")
        # set the icon
        self.icon = tk.PhotoImage(file = '.\\icon.png')
        master.iconphoto(False, self.icon)
        # initialise the nasa api object
        self.api = nasa_api()
        self.master = master
        self.im = None
        # create all the widgets which will be used
        self.create_widget()
        self.bind("<Configure>",self._resize)
