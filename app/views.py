from app import app
from secrets import secret_payload
from flask import request, flash, abort, render_template
from forms import SubmissionForm
import requests
from requests.exceptions import HTTPError


@app.route('/', methods=['GET', 'POST'])
def submission():
    submission_form = SubmissionForm(request.form)

    if request.method == 'POST':
        url = submission_form.submission_url.data
        payload = secret_payload
        r = requests.post(url=url, data=payload)

        try:
            r.raise_for_status()
        except HTTPError:
            flash(message='Your API returned an error.', category='error')
            abort(502)

        flash('Successfully posted payload. Happy hunting.')

    return render_template('submission.html', form=submission_form)