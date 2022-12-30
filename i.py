from flask import Flask,redirect,jsonify,render_template,request,url_for
from utils import LoanData
import config

app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('welcome to loan status prediction')
    return render_template('index.html')

@app.route('/status',methods=['GET','POST'])
def get_status():
    if request.method=='POST':
        data=request.form
        print('Data',data)

        result=LoanData(data)
        output = result.predict_loan_status()
        # return jsonify({'Status': output})
        return render_template('index.html',prediction=output)
    else:
        data=request.form
        print('Data',data)

        result=LoanData(data)
        output = result.predict_loan_status()
        # return jsonify({'Status': output})
        return render_template('index.html',prediction=output)

if __name__=='__main__':
    app.run(host= "0.0.0.0", port= config.PORT_NUMBER)