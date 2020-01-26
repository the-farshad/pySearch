from image import save_image

search_string = "\n\tInsert you text > "
bing = "https://www.bing.com/images/search"
google = ""
ddg = ""

def main():
    search_input = input(search_string)
    engine_params = {"q": search_input}
    save_image(bing, engine_params, search_input)

if __name__ == "__main__":
    main()
