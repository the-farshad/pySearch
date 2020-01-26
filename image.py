from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def save_image(search_engines, params, search_word):
    image_requests = requests.get(search_engines, params=params)
    soup = BeautifulSoup(image_requests.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    images_dir = "./images/" + search_word.replace(" ", "-").capitalize()

    if not os.path.isdir(images_dir):
        os.makedirs(images_dir)

    for item in links:
        try:
            image_object = requests.get(item.attrs["href"])
            print("Getting > ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            image_link = Image.open(BytesIO(image_object.content))
            image_link.save(images_dir + "/" + title, image_link.format)
        except:
            print("Sorry Buddy, could not save this image :) ")
