from flask import Flask,redirect,jsonify,render_template,request,url_for
from utils import LoanData
import config

app = Flask(__name__)


@app.route('/predict_status',methods=['GET','POST'])
def get_status():
    if request.method=='POST':
        data=request.form
        print('Data',data)

        result=LoanData(data)
        output = result.predict_loan_status()
        return jsonify({'Status': output})
    
if __name__=='__main__':
    app.run()