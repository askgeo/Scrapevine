# Wikidata Scraper: Lake Stats
# Abigail Knapp 11/2021
# some code snippets from # at https://realpython.com/python-web-scraping-practical-introduction
# and Code snippet from https://stackoverflow.com/
# # questions/26476446/how-to-extract-the-infobox-vcard-from-wikipedia-using-the-python-wikipedia-libra
from typing import Dict, Any

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import enum

# -------------INPUTS

# Base url and list of pages to parse
BASE_URL = "https://www.wikidata.org/wiki/"
SUB_PAGE1 = 'Q182796'
SUB_PAGE2 = 'Q1801004'
SUB_PAGE3 = 'Q23883'
SUB_PAGES = {
    "Lake Nasser": "Q182796",
    "Lake Mendota": "Q1801004",
    "Dead Sea": "Q23883",
}

# -------------FUNCTIONS

def make_soup(BASE_URL, SUB_PAGE):
    page_url = BASE_URL + SUB_PAGE
    html = urlopen(page_url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_info(soup):
    elevation_name = 'Elevation above sea level'
    elevation_id = 'P2044'
    elevation_class = 'wikibase-snakview-value wikibase-snakview-variation-valuesnak'
    elevation = soup.find('div', id=elevation_id).find('div', class_=elevation_class).text

    coords_name = 'Coordinates'
    coords_class = 'wikibase-kartographer-caption'
    coords = soup.find('div', class_=coords_class).text

    info_dict = {
        coords_name: coords,
        elevation_name: elevation,
    }
    return info_dict

# -------------PROCESS

#Make soup object, get the info as a dictionary, then print it

soup = make_soup(BASE_URL, SUB_PAGE1)
info = get_info(soup)
print(info)

soup = make_soup(BASE_URL, SUB_PAGE2)
info = get_info(soup)
print(info)

soup = make_soup(BASE_URL, SUB_PAGE3)
info = get_info(soup)
print(info)

# -------------MORE TESTING HERE



# -- TEST LATER

# Attempted to make a loop which creates a dictionary of dictionaries

# info_of_info = {}
# for lake in SUB_PAGES.values():
#     sub_page_id = str(SUB_PAGES.values())
#     soup = make_soup(BASE_URL, sub_page_id)
#     info: dict[Any, Any] = get_info(soup)
#     info_of_info[SUB_PAGES.items()] = info
# print(info_of_info)

# Attempted to make a class for lake info with methods that get the lake info

# class SoupInfo(self, soup, sub_page):
#     elevation_name = 'Elevation above sea level'
#     elevation_id = 'P2044'
#     elevation_class = 'wikibase-snakview-value wikibase-snakview-variation-valuesnak'
#
#     coords_name = 'Coordinates'
#     coords_class = 'wikibase-kartographer-caption'
#
#     def __init__(self):
#         self.elevation = soup.find('div', id=elevation_id).find('div', class_=elevation_key).text
#         self.coords = soup.find('div', class_=coords_class).text
#
#     @property
#     def get_info(self):
#         info_dict = {
#             coords_name: self.coords,
#             elevation_name: self.elevation,
#         }
#         return info_dict
#
#
# x = SoupInfo(soup, sub_page)
# print(get_info(x))


