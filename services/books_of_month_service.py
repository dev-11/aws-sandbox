import requests
import bs4


class BooksOfTheMonthService:
    def __init__(self, url):
        self._url = url

    @staticmethod
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

    def get_books_of_the_month(self):
        page = requests.get(self._url)

        soup = bs4.BeautifulSoup(page.text, 'html.parser')

        lst = soup.find(class_='row home-row')
        lst2 = lst.find_all(class_='span12')

        bom = lst2[1:]
        grouped = list(zip(*[iter(bom)] * 2))

        return [self.get_book_details(pair) for pair in grouped]
