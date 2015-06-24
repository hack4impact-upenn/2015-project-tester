from flask.ext.wtf import Form
from wtforms.validators import URL
from wtforms import StringField


class SubmissionForm(Form):
    submission_url = StringField(
        label='API URL',
        validators=URL(message='Invalid URL'),
    )