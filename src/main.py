import tkinter as tk
import requests
import json
import PIL.Image
import PIL.ImageTk

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
    def change_img(self):
        self.img = PIL.ImageTk.PhotoImage(self.im)
        self.lab.config(image=self.img)
    def create_widget(self):
        # create the get image button.
        tk.Button(text="get image", command=self.open_image).pack()
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
        self.im = PIL.Image.open(requests.get(link, stream=True).raw)
        # display the image
        self.change_img()
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        # initialise the nasa api object
        self.api = NASA_API()
        self.master = master
        # create all the widgets which will be used
        self.create_widget()

if(__name__== "__main__"):
    # api = NASA_API() 
    # print(api.get_photo_link())
    root = tk.Tk()
    app = Application(root)
    root.mainloop()