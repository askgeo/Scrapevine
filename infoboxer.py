# Get Wikipedia Infobox and put into dictionary
# Abigail Knapp 11/2021
# Code snippet from https://stackoverflow.com/
# questions/26476446/how-to-extract-the-infobox-vcard-from-wikipedia-using-the-python-wikipedia-libra

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import enum

#-------------FUNCTIONS

def make_soup(base_url, page):
    page_url = base_url + page
    html = urlopen(page_url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_box(soup):
    infobox = soup.find('table', {'class': 'infobox'})
    return infobox

def get_boxdict(soup, sub_page):
    infobox_dict = {
        "Name": sub_page.replace("_", " "),
        "Coords": soup.find('span', class_='geo-dec').text,
    }
    return infobox_dict

def souptostr(soup_obj):
    for item in soup_obj:
        print(str(item.text))

#-------------TAKE INPUT

# Enter base url and list of pages to parse, list links, list images, pull name
base_url = "https://en.wikipedia.org/wiki/"
sub_page = 'Lake_Erie'

#-------------PROCESS

# Make soup object, get the wiki infobox, then make a base dictionary
soup = make_soup(base_url, sub_page)
box_dict = get_boxdict(soup, sub_page)



#for key, value in box_dict.items():
    #print(key, value)

#-------------MORE TESTING HERE

# Look at all tr pieces in the infobox
infobox_obj = get_box(soup)
infobox_pieces = infobox_obj.find_all('td')
#infobox_str = souptostr(infobox_pieces)
print(infobox_obj.get_text())
#print(infobox_str)

# Sample strings.
list = ["dog dot", "data day", "no match"]

# Loop.
for element in list:
    # Match if 2 words starting with letter "d."
    m = re.match("(dog dot)", element)

    # See if success.
    if m:
        print(m.groups())

#for piece in infobox_pieces:
    #m = re.match(pattern, piece)
    #if m:
        #print(m.groups())

#-------------SAVE FILES