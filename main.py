from bs4 import BeautifulSoup
from urllib.request import urlopen
import constants as c
import configs as u
from dataclasses import dataclass

# -------------DATA CONTAINERS


@dataclass
class ScrapedData:
    # Data container for each scraped page, defaulting to the 'Q182796' page
    name: str = ' '
    coords: str = ' '
    elevation: int = 99999
    inflow_name: str = ' '
    outflow_name: str = ' '
    data_id: str = ' '


# -------------FUNCTIONS


def get_user_pages():
    # Take user input until user hits ENTER
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


def make_soup(base_url, subpage):
    # Make a Beautiful Soup tag object from the base url and page from user defined ID
    page_url = base_url + subpage
    html = urlopen(page_url).read().decode("utf-8")
    soup_object = BeautifulSoup(html, "html.parser")
    return soup_object


def separate_coords():
    # Comment
    pass


def scrape_data(soup_object):
    # Using the constant tags, scrape statistics for a Wikidata ID's page
    ele_val = soup_object.find('div', id=c.ELE_ID).find('div', class_=c.ELE_CLASS).text
    coords_val = soup_object.find('div', class_=c.COORDS_CLASS).text
    stats_list = [coords_val, ele_val, ]
    return stats_list


def scrape_data_to_class(soup_object, subpage):
    # Using the constant tags, scrape statistics for a Wikidata ID's page
    ele_val = soup_object.find('div', id=c.ELE_ID)\
        .find('div', class_=c.ELE_CLASS)\
        .text
    coords_val = soup_object.find('div', class_=c.COORDS_CLASS)\
        .text.replace(',', '')
    stats_instance = ScrapedData(
        data_id=subpage,
        coords=coords_val,
        elevation=ele_val,
    )
    return stats_instance


def scrape_data_to_dict(soup_object):
    # Using the constant tags, scrape statistics for a Wikidata ID's page
    ele_val = soup_object.find('div', id=c.ELE_ID).find('div', class_=c.ELE_CLASS).text
    coords_val = soup_object.find('div', class_=c.COORDS_CLASS).text
    stats_dict = {
        'Coordinates:': coords_val,
        'Elevation above sea level:': ele_val,
    }
    return stats_dict


# -------------USER INPUT

pages = get_user_pages()


# -------------PROCESS

# Make soup object, get the info as a dataclass instance, then print it
# Need to refactor the following to functions, configs, and constants
data_list = []

for page in pages:
    try:
        soup = make_soup(base_url=c.BASE_URL, subpage=page)
        ele_val = soup.find('div', id=c.ELE_ID).find('div', class_=c.ELE_CLASS).text
        coords_val = soup.find('div', class_=c.COORDS_CLASS).text.replace(',', '')
        name_val = 'name_placeholder'
        #put the scraped data into a dataclass and then into the list
        stats = ScrapedData(name=name_val, coords=coords_val, elevation=ele_val, data_id=page)
        data_list.append(stats)
    except:
        print('That doesn\'t seem to be a valid ID. Please try again later.')

#print(f"\nSuccess! For example, the lake named {data_list[0].name} is at {data_list[0].coords} and "
#      f"\nis approximately {data_list[0].elevation}s above sea level. \n")

headers = 'data_id;name;coordinates;elevation'
print(headers)
for thing in data_list:
    line = f"{thing.data_id};{thing.name};{thing.coords};{thing.elevation}"
    ######need to append these lines to a list and then save as a text document

# Make a csv file and download it
