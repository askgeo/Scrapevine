# scrapevine, a First Webscraper Project
# Webscraper tutorial code, refactored into a program by Abigail Knapp
# Project basis and code snippets from realpython tutorial
# at https://realpython.com/python-web-scraping-practical-introduction
# Abigail Knapp 11/2021

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#-----------------------------------
#-------------WITHOUT BEAUTIFUL SOUP
#-----------------------------------

# Pick a webpage and open, read bytes, and decode to characters
def get_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

# Method 1: Find a pattern on a webpage and print the value after the pattern until the first tag
def find_value(html, keyword):
    pattern = keyword + ".*?<"
    match_results = re.search(pattern, html, re.IGNORECASE)
    i = match_results.group()
    j = re.sub(keyword, "", i) # Removes search term wrappers #1
    k = re.sub("<", "", j) # Removes search term wrappers #2
    result = k.strip()
    return result

#html = get_html("http://olympus.realpython.org/profiles/dionysus")
#print(html)
#print(find_value(html, "Favorite animal:"))

# Method 2: Find a pattern on a webpage and print the value after the pattern until the first tag
def find_values(keywords):
    for string in keywords:
        string_start_idx = html.find(string)
        text_start_idx = string_start_idx + len(string)

        next_tag_idx = html[text_start_idx:].find("<")
        text_end_idx = text_start_idx + next_tag_idx
        raw_text = html[text_start_idx:text_end_idx]
        clean_text = raw_text.strip()
        return clean_text

#to_find = ["Name:", "Favorite Color:", "animal:"]
#print(find_values(to_find))

#-----------------------------------
#-------------WITH BEAUTIFUL SOUP---
#-----------------------------------

# Use BS4 to parse html and list images and links
def make_soup(base_url, page):
    page_url = base_url + page
    html = urlopen(page_url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print("\n", f"The url is: {base_url}{page}")
    return soup

def list_links(soup, base_url):
    links = soup.find_all("a")
    if not links:
        print("\n", "There are no links on this page.")
    else:
        print("\n", "The links are: ")
        for link in links:
            link_url = base_url + link["href"]
            print(link_url)

def list_imgs(soup):
    images = soup.find_all("img")
    if not images:
        print("\n", "There are no images on this page.")
    else:
        print("\n", "The images are: ")
        count = 0
        for img in images:
            print("\n", count, img["src"])
            count += 1

def list_value(soup, keywords):
    pass

# Enter base url and list of pages to parse, list links, list images, pull name
base_url = "http://olympus.realpython.org"
pages = ["/profiles", "/profiles/aphrodite", "/profiles/dionysus", "/profiles/poseidon"]

for page in pages:
    soup = make_soup(base_url, page)
    list_links(soup, base_url)
    list_imgs(soup)

# Next step - make a function that takes in base_url and an index page and loops through each link, pulling out
# the images and links in each one!

# Then also make list_value work

# Should I make a class?

# Next step after that, start testing on Wikipedia

