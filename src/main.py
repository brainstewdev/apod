import tkinter as tk
from tkinter.constants import RIGHT

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

class Application_prova(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widg()

    def create_widg(self):
        # button to get the picture
        self.get_photo_button = tk.Button(self)
        self.get_photo_button["text"] = "get the Picture"
        self.get_photo_button["command"] = None
        self.get_photo_button.pack(side="bottom")

        # button to save the photo
        self.save_photo_button = tk.Button(self)
        self.save_photo_button["text"] = "save the photo"
        self.save_photo_button["state"] = "disabled"
        self.save_photo_button.pack(side="right")
    


root = tk.Tk()
app = Application_prova(master=root)
app.mainloop()