from app import app
from flask import request, flash, render_template, redirect, url_for, jsonify
from forms import SubmissionForm
from tasks import make_requests_to_api


@app.route('/')
def index():
    submission_form = SubmissionForm(request.form)
    return render_template('submission.html', form=submission_form)


@app.route('/start_request', methods=['POST'])
def start_request():
    url = request.form['url']
    task = make_requests_to_api.delay(url)
    return url_for('task_status', task_id=task.id), 200


@app.route('/status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = make_requests_to_api.AsyncResult(task_id)
    response = {
        'exception': str(task.result),
        'state': task.state,
    }
    return jsonify(response)
