# Wikipedia Page Scraper: Lake Stats
# Abigail Knapp 11/2021

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#-------------FUNCTIONS

def scrape_if(get_var):
    if get_var is not None:
        set_var = get_var.text
    else:
        set_var = []
    return set_var

def make_soup(base_url, page):
    page_url = base_url + page
    html = urlopen(page_url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

def lake_descrip(sub_page):
    name = sub_page.replace('_', ' ')
    coords = scrape_if(soup.find('span', class_='geo-dec'))
    return name, coords



def lake_type(sub_page):
    pass

def lake_metrics():
    pass

#-------------TAKE INPUT
# Enter base url and list of pages to parse, list links, list images, pull name
base_url = "https://en.wikipedia.org/wiki/"

#-------------PROCESS


#-------------REFACTOR THIS AFTER TESTING

# Save place: all of this section... trying to use grep or regex or something
# To do that, I really should use some sort of custom thing to
# check whether a key word is there (ie the title, like "Location"
# and then take the next <tr> tag's text.

nasser = 'Lake_Nasser'
pabor = ['Pabor_Lake', ]
florida = ['Lake_Washington_(Florida)', 'Lake_Okeechobee', 'Pabor_Lake']
egypt = ['Lake_Nasser', 'Lake_Mariout', 'Lake_Manzala']

for lake in egypt:
    soup = make_soup(base_url, lake)
    print(lake_descrip(lake))
    #print(lake_type(lake)) # Need to figure this out, see infobox method in progress
    # below and notes above

soup = make_soup(base_url, nasser)
#print(soup)

def infobox(soup):
    infobox = soup.find('table', {'class': 'infobox'})
    return infobox

infobox = infobox(soup)

for tr in infobox.find_all('tr'):
    print(tr.text)

#-------------MORE TESTING HERE


#-------------SAVE FILES

