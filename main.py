from bs4 import BeautifulSoup
from urllib.request import urlopen
import constants as c
import configs as u

# -------------FUNCTIONS

# Take user input until user hits ENTER
def get_user_pages():
    i = 0
    user_pages = []
    input_active = True
    print('Type a Wikidata ID, or hit ENTER to continue.')
    while input_active is True:
        user_page_input = input('ID:')
        if i == 0 and user_page_input == '':
            print("\nOK, using the default IDs....")
            user_pages = u.default_pages
            input_active = False
        elif user_page_input == '':
            print("Thanks, scraping the statistics....")
            input_active = False
        else:
            add_page = str(user_page_input)
            user_pages.append(add_page)
            print("Type another ID, or hit ENTER to continue..")
            i += 1
    print(f'\nNow scraping: {user_pages}.\n')
    return user_pages

# Make a Beautiful Soup object from the base url and page from user defined ID
def make_soup(base_url, subpage):
    page_url = base_url + subpage
    html = urlopen(page_url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

# Using the constant tags, scrape statistics for a Wikidata ID's page
def scrape_data(soup):
    ele_val = soup.find('div', id=c.ELE_ID).find('div', class_=c.ELE_CLASS).text
    coords_val = soup.find('div', class_=c.COORDS_CLASS).text
    data_dict = {
        c.COORDS_NAME: coords_val,
        c.ELE_NAME: ele_val,
    }
    return data_dict

# -------------USER INPUT

pages = get_user_pages()

# -------------PROCESS

# Make soup object, get the info as a dictionary, then print it
for page in pages:
    try:
        soup = make_soup(c.BASE_URL, page)
        data = scrape_data(soup)
        print(data)
    except:
        print('That doesn\'t seem to be a valid ID. Please try again later.')

# Make a csv file and download it
