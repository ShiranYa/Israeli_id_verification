from flask import Flask, render_template, request
from validation_id import validation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods= ['POST'])
def submit():
    body_request_id = request.json['id']
    result_validation = validation(body_request_id)
    return result_validation


if __name__ == '__main__':
    app.run(debug=True)



