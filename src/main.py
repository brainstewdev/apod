import tkinter as tk
import requests
import json
from PIL import ImageTk, Image


class NASA_API():
    def __init__(self, file_path="./key"):
        # initialise base informations

        # setup the base link for the requests
        self.base_link = "https://api.nasa.gov/planetary/apod?api_key="

        # read the api from the file
        self.api_key = ""
        with open(file_path,"r") as f:
            try:
                self.api_key = f.readline()
            except FileNotFoundError:
                print("ERROR: file for the API key was not found")
                quit()
        # if the api_key is empty then quit
        if(self.api_key == ""):
            print("ERROR: couldn't get the API key")
            quit()

    def get_photo_link(self):
        # return the image link by parsing the json
        
        # get the json from NASA api
        j = json.loads(self.get_APOC_json())
        
        # print(j)

        if(j["media_type"] == "image"):
            return j["hdurl"]
        pass
    def get_APOC_json(self):
        r = requests.get(self.base_link+self.api_key)

        if(r.status_code != 200):
            return False
        else:
            return r.text

class Application(tk.Frame):
    # constructor for the class
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.api = NASA_API() 
    # function used to create the widgets and putting them into the frame
    def create_widgets(self):
        print("creo widgets")
        # button to get the picture
        self.get_photo_button = tk.Button(self)
        self.get_photo_button["text"] = "get the Picture"
        self.get_photo_button["command"] = self.put_image_on_label
        self.get_photo_button.pack()

        # button to save the photo
        self.save_photo_button = tk.Button(self)
        self.save_photo_button["text"] = "save the photo"
        self.save_photo_button["state"] = "disabled"
        self.save_photo_button.pack()

        self.lbl = tk.Label(self)
        self.lbl.pack()
    def put_image_on_label(self):
        link = api.get_photo_link()
        img = ImageTk.PhotoImage(Image.open(requests.get(link, stream=True).raw))
        self.lbl["image"] = img

if(__name__== "__main__"):
    api = NASA_API() 
    print(api.get_photo_link())
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()