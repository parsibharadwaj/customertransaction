import joblib

def predict_tran(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10):
    model = joblib.load('customer_deploy.pkl')
    prediction = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]])
    
    if prediction == 0:
        return 'NO, the Customer will not Transact in future'
    
    elif prediction == 1:
        return 'YES, the Customer will do Transactions in future'


import flask
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    #extract data from post request
    v1 = float(request.form['v1'])
    v2 = float(request.form['v2'])
    v3 = float(request.form['v3'])
    v4 = float(request.form['v4'])
    v5 = float(request.form['v5'])
    v6 = float(request.form['v6'])
    v7 = float(request.form['v7'])
    v8 = float(request.form['v8'])
    v9 = float(request.form['v9'])
    v10 = float(request.form['v10'])
    print (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10)
    prediction = predict_tran(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10)
    return render_template('predict.html', transaction=prediction)

if __name__ == '__main__':
    app.run()
