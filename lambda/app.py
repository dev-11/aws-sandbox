import json
from datetime import datetime as dt


def lambda_handler(event, context):
    response = {'event': event,
                'context': context,
                'payload': dt.now()}

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
