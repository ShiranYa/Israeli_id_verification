import json
from flask import Flask, render_template, request
from validation_id import validation

app = Flask(__name__)

id_cache = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods= ['POST'])
def submit():
    body_request_id = request.json['id']
    if body_request_id in id_cache:
        return id_cache[body_request_id]
    result_validation = validation(body_request_id)
    id_cache[body_request_id] = result_validation

    return result_validation

if __name__ == '__main__':
    app.run(debug=True)



