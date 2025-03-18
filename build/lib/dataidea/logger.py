import requests

def log_event(data:dict):
    '''
    Log an event to the DATAIDEA LOGGER API

    parameters:
    data: dict

    eg:
    data = {
        'api_key': '1234567890',
        'user_id': '1234567890',
        'message': 'This is a test message',
        'level': 'info',
        'metadata': {'test': 'test'}
    }
    '''
    url = 'https://loggerapi.dataidea.org/event-log'
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print('Event logged successfully')
    else:
        print('Failed to log event')

def get_event_logs(api_key:str):
    '''
    Get event logs from the DATAIDEA LOGGER API

    parameters:
    api_key: str

    eg:
    api_key = '1234567890'
    '''
    url = 'https://loggerapi.dataidea.org/event-log'
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
    return response.json()


def log_llm_event(data:dict):
    '''
    Log an LLM event to the DATAIDEA LOGGER API

    parameters:
    data: dict

    eg:
    data = {
        'api_key': '1234567890',
        'user_id': '1234567890',
        'source': 'llm',
        'query': 'This is a test query',
        'response': 'This is a test response',
    }
    '''
    url = 'https://loggerapi.dataidea.org/llm-log'
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print('LLM event logged successfully')
    else:
        print('Failed to log LLM event')


def get_llm_event_logs(api_key:str):
    '''
    Get LLM event logs from the DATAIDEA LOGGER API

    parameters:
    api_key: str
    '''
    url = 'https://loggerapi.dataidea.org/llm-log'
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
    return response.json()


if __name__ == '__main__':
    log_event({
        'api_key': '1234567890',
        'user_id': '1234567890',
        'message': 'This is a test message',
        'level': 'info',
        'metadata': {'test': 'test'}
    })

    log_llm_event({
        'api_key': '1234567890',
        'user_id': '1234567890',
        'source': 'llm',
    })