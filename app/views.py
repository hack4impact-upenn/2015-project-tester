from app import app
from secrets import secret_payload
from flask import request, flash, render_template, redirect, url_for
from forms import SubmissionForm
import requests


@app.route('/', methods=['GET', 'POST'])
def submission():
    submission_form = SubmissionForm(request.form)

    if request.method == 'POST':
        url = submission_form.submission_url.data
        payload = secret_payload
        r = requests.post(url=url, data=payload)

        r.raise_for_status()

        flash('Successfully posted payload. Happy hunting.', category='info')

    return render_template('submission.html', form=submission_form)

@app.errorhandler(Exception)
def error(an_error):
    flash(message='Your API returned an error: ' + str(an_error), category='danger')
    return redirect(url_for('submission'))