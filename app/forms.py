from flask.ext.wtf import Form
from wtforms.validators import URL, DataRequired
from wtforms import StringField, SubmitField


class SubmissionForm(Form):
    submission_url = StringField(
        label='API URL',
        validators=[URL(message='Invalid URL'), DataRequired()],
    )
    submit_field = SubmitField(
        label='Submit'
    )