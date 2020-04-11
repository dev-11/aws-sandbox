from datetime import datetime as dt
from services import BooksOfTheMonthService
import json
import config


def lambda_handler(event, context):

    data = get_books_of_month()

    return {
        'statusCode': 200,
        'body': {
            'fetched_at': json.dumps(f'{dt.now()}'),
            'data': [data]
        }
    }


def get_books_of_month():
    bom_service = BooksOfTheMonthService(config.books_of_the_month_url)
    books_of_the_month = bom_service.get_books_of_the_month()

    return {
        'service': 'book_of_the_month',
        'data': books_of_the_month
    }
