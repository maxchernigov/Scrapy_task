import requests
from bs4 import BeautifulSoup

# from connection import connect

domain = "http://quotes.toscrape.com/"
url = "http://quotes.toscrape.com/"
response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")
# print(response.text)
html = soup.prettify()
list_author = []


def scrapy_quote():
    quotes = soup.find_all("div", class_="quote")

    list_quotes = []

    for i in quotes:
        tags = []
        result_quotes = i.find("span").text.replace("\u00e9", "e")
        result_author = i.find("small", class_="author").text.strip()
        author_url = domain + i.a["href"]
        scrap_author(author_url)

        result_tags = i.find_all("a", class_="tag")

        for tag in result_tags:
            tags.append(tag.text)
            quote_dict = {
                "tags": tags,
                "authors": result_author,
                "quote": result_quotes.replace("\u00e9", "e"),
            }
        list_quotes.append(quote_dict)
        print(list_quotes)
    return list_quotes


def scrap_author(author_url):
    author_response = requests.get(author_url)
    author_soup = BeautifulSoup(author_response.text, features="html.parser")

    authors = author_soup.find_all("div", class_="author-details")
    for author in authors:
        result_name = author.find("h3").text
        result_date = author.find("span", class_="author-born-date").text
        result_location = author.find("span", class_="author-born-location").text
        result_description = author.find(
            "div", class_="author-description"
        ).text.strip()
        list_author.append(
            {
                "fullname": result_name,
                "born_date": result_date,
                "born-location": result_location,
                "description": result_description,
            }
        )
        # print(list_author)
    return list_author
