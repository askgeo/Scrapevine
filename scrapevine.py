# Scrapevine, a First Webscraper Project
# Project basis and code snippets from realpython tutorial at https://realpython.com/python-web-scraping-practical-introduction
# Abigail Knapp 11/2021

from urllib.request import urlopen
import re

# Pick a webpage and open, read bytes, and decode to characters
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Print webpage html
#print(html)

# Using regex, pull out just the html with title tags, accounting for mistyped html
#pattern = "<title.*?>.*?</title.*?>"
#match_results = re.search(pattern, html, re.IGNORECASE)
#title = match_results.group()
#title = re.sub("<.*?>", "", title) # Removes HTML tags
#print(title)

# Find favorite animal and color
animal_pattern = "animal:.*?<*?br*?>"
animal_match_results = re.search(animal_pattern, html, re.IGNORECASE)
animal1 = animal_match_results.group()
#print(animal1)
animal2 = re.sub("animal:", "", animal1) # Removes search term wrappers #1
#print(animal2)
animal_result = re.sub("<*?br*?>", "", animal2) # Removes search term wrappers #2
print(animal_result)

# Find favorite animal and color
name_pattern = "Name:.*?<*?br*?>"
name_match_results = re.search(name_pattern, html, re.IGNORECASE)
name1 = name_match_results.group()
name2 = re.sub("Name:", "", name1) # Removes search term wrappers #1
name_result = re.sub("<*?br*?>", "", name2) # Removes search term wrappers #2
print(name_result)

