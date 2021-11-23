# scrapevine, a First Webscraper Project
# Project basis and code snippets from realpython tutorial
# at https://realpython.com/python-web-scraping-practical-introduction
# Abigail Knapp 11/2021

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Pick a webpage and open, read bytes, and decode to characters
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Find favorite animal using regex
animal_pattern = "animal:.*?<*?br*?>"
animal_match_results = re.search(animal_pattern, html, re.IGNORECASE)
animal1 = animal_match_results.group()
#print(animal1)
animal2 = re.sub("animal:", "", animal1) # Removes search term wrappers #1
#print(animal2)
animal_result = re.sub("<*?br*?>", "", animal2) # Removes search term wrappers #2
animal_clean = animal_result.strip()
#print(animal_clean)

# Find name and favorite color using a loop
to_find = ["Name:", "Favorite Color:"]
for string in ["Name:", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_tag_idx = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_tag_idx
    raw_text = html[text_start_idx:text_end_idx]
    clean_text = raw_text.strip()
    assert isinstance(clean_text, object)
    #print(clean_text)

# Use BS4 to pull all image srcs from the page
soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text().replace("\n", " "))
images = soup.find_all("img")
count = 0
for img in images:
    print("\n", count, img["src"])
    count += 1

print("And then...")

# Use BS4 to pull links from a page
base_url = "http://olympus.realpython.org"
url_page = base_url + "/profiles"
page = urlopen(url_page)
html_bytes2 = page.read()
html2 = html_bytes2.decode("utf-8")

soup = BeautifulSoup(html2, "html.parser")
#print(soup.get_text().replace("\n", " "))

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)

def make_soup(base_url, page):
    base = base_url
    page_url = base_url + page
    page_stuff = urlopen(page_url)
    html_bytes = page_stuff.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

soup2 = make_soup("http://olympus.realpython.org", "/profiles")
for link in soup2.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)



