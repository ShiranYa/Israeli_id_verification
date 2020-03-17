from flask import Flask, render_template, request,js,jsonify,make_response
from validation_id import validation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    id = request.json['id']
    status = validation(id)
    return status

if __name__ == '__main__':
    app.run(debug=True)



