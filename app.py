from time import sleep
import json
import pprint

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
    sleep(2)
    id_cache[body_request_id] = result_validation
    try:
        with open('id_cache.txt', 'r+') as id_file:
            json.dump(id_cache, id_file, indent=1)
    except Exception as e:
        print(str(e))

    return result_validation

if __name__ == '__main__':
    app.run(debug=True)



