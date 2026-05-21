"""Download and save image-search results to a local folder."""

import os
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from PIL import Image


def save_image(search_engine, params, search_word):
    response = requests.get(search_engine, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    images_dir = os.path.join(
        "images", search_word.replace(" ", "-").capitalize()
    )
    os.makedirs(images_dir, exist_ok=True)

    for item in links:
        href = item.attrs["href"]
        try:
            print("Getting >", href)
            image_response = requests.get(href)
            title = href.split("/")[-1]
            image = Image.open(BytesIO(image_response.content))
            image.save(os.path.join(images_dir, title), image.format)
        except Exception:
            print("Could not save this image:", href)
