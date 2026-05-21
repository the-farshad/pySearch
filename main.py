"""Search Bing Images for a phrase and save the results locally."""

from image import save_image

BING_IMAGES_URL = "https://www.bing.com/images/search"


def main():
    search_input = input("\n\tInsert your text > ")
    save_image(BING_IMAGES_URL, {"q": search_input}, search_input)


if __name__ == "__main__":
    main()
