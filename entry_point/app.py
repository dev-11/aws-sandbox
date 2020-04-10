import json
from datetime import datetime as dt
import bs4
import requests


def lambda_handler(event, context):
    data = get_section()

    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda @ {dt.now()}, {data}!')
    }


def get_book_details(divs):
    section = divs[0].find('h2').find('em').text
    title = divs[1].find(class_='title').find('a').text
    return section, title


def get_section():
    site = 'https://www.waterstones.com/campaign/books-of-the-month'
    page = requests.get(site)

    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    lst = soup.find(class_='row home-row')
    lst2 = lst.find_all(class_='span12')

    bom = lst2[1:]
    v = bom[0:2]

    return get_book_details(v)
