#!/usr/bin/env python3

import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as output:
        output.write(get_response.content)

download("https://i.pinimg.com/originals/db/7e/bf/db7ebf1be06dd0fa7c44e70f104d1bc1.jpg")
