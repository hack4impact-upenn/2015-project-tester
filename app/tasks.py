from secrets import secret_payload
import requests
from app import celery


@celery.task(bind=True)
def make_requests_to_api(self, url):
    # try:
    payload = secret_payload
    r = requests.post(url=url, json=payload)
    r.raise_for_status()
    # except Exception as an_error:
    #     message = 'Your API returned an error: ' + str(an_error)
    #     self.update_state(state='FAILURE', meta={'message': message})