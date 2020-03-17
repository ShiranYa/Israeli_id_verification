from flask import Flask, render_template, request
from validation_id import validation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods= ['GET','POST'])
def submit():
    id = str(request.json)
    status = validation(id)
    if status==True:
        return 'Your ID is valid'
    elif  status==False: return 'Your ID is NOT valid'
    else: return status #is this the way to close completly the valdation on the server side?

if __name__ == '__main__':
    app.run(debug=True)



