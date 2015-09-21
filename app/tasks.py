from secrets import secret_payload
import requests
from app import celery


@celery.task()
def make_requests_to_api(url):
    # Make sure the api is alive
    get = requests.get(url=url + '/health')
    get.raise_for_status()

    # Now make post request
    payload = secret_payload
    post = requests.post(url=url + '/coordinates', json=payload)
    post.raise_for_status()
    print 'Made request to {}. Awesome!'.format(url)
