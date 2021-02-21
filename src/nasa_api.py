import requests
import json

class nasa_api():
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
        if(j["media_type"] == "image"):
            return j["hdurl"]
        pass
    def get_APOC_json(self):
        r = requests.get(self.base_link+self.api_key)
        if(r.status_code != 200):
            return False
        else:
            return r.text
    def get_stream_from_link(self, link):
        return requests.get(link, stream=True).raw
