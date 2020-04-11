from datetime import datetime as dt
import bs4
import requests


def lambda_handler(event, context):
    data = get_section()

    return {
        'statusCode': 200,
        'body': {
            'fetched_at': dt.now(),
            'data': data
        }
    }


def get_book_details(divs):
    section = divs[0].find('h2').find('em').text.strip()
    title = divs[1].find(class_='title').find('a').text.strip()
    authors = divs[1].find(class_='authors').find('a').text.strip()
    price = divs[1].find('b', itemprop='price').text.strip()
    frmat = divs[1].find(class_='format').text.strip()
    desc = divs[1].find(class_='description').text.strip()
    return {
        'section': section,
        'title': title, 
        'authors': authors,
        'price': price,
        'format': frmat,
        'desc': desc
    }


def get_section():
    site = 'https://www.waterstones.com/campaign/books-of-the-month'
    page = requests.get(site)

    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    lst = soup.find(class_='row home-row')
    lst2 = lst.find_all(class_='span12')

    bom = lst2[1:]
    grouped = list(zip(*[iter(bom)] * 2))

    sections = []
    for pair in grouped:
        sections.append(get_book_details(pair))

    return sections
