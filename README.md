# Scrapelake
Scrapelake is a web scraping program to make dat dictionaries from WikiData pages. 

Scrapelake is written in Python using BeautifulSoup, and currently pulls from pages about lakes.

## Scraping Wikidata for lake statistics

### How to use Scrapelake:

1. Run main.py and enter in a list of wikidata page IDs corresponding to lakes to scrape.
</br>1.a. Or, run vignette.py as an example.
2. Confirm options, such as whether to download the results.
3. Enjoy your new data file!

**Credit where credit is due:**</br>
Some code snippets from </br>
https://realpython.com/python-web-scraping-practical-introduction
</br>
and from </br>
https://stackoverflow.com/questions/26476446/how-to-extract-the-infobox-vcard-from-wikipedia-using-the-python-wikipedia-libra

**Feature To-Do List:**

* Take user input for the WikiData page IDs to scrape, then:
1. Take user input of lake names, and search and pull the WikiData page IDs
2. Loop over an input dictionary of WikiData pages
* Save the data dictionaries as entries in a table
* Save the table as a CSV and download
* Package in a GUI and .exe for easy sharing