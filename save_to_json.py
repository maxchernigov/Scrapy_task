import json
from scrapy import scrap_author, scrapy_quote, list_author


def save_f():
    with open("quotes.json", "w") as file:
        json.dump(scrapy_quote(), file, indent=4)
    print("quote.json saved")

    with open("authors.json", "w") as file:
        json.dump(list_author, file, indent=4)
    print("author.json saved")


if __name__ == "__main__":
    save_f()
