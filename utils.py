import pickle
import json
import config
import numpy as np

class LoanData():

    def __init__(self,user_data):
        self.model_path=config.model_path
        self.user_data=user_data

    def load_saved_data(self):
        with open(self.model_path,'rb') as f:
            self.model=pickle.load(f)

        with open(config.project_data_path,'r') as f:
            self.project_data=json.load(f)

    def predict_loan_status(self):
        self.load_saved_data()
        Gender=self.user_data['Gender']
        Married=self.user_data['Married']
        Education=self.user_data['Education']
        Self_Employed=self.user_data['Self_Employed']
        Dependents=self.user_data['Dependents']
        Property_Area=self.user_data['Property_Area']

        Gender=self.project_data['Gender'][Gender]
        Married=self.project_data['Married'][Married]
        Education=self.project_data['Education'][Education]
        Self_Employed=self.project_data['Self_Employed'][Self_Employed]
        
        Dependents='Dependents_'+Dependents
        Dependents_index=np.where(np.array(self.project_data['columns'] == Dependents))[0]

        Property_Area='Property_Area_'+Property_Area
        Property_Area_index=np.where(np.array(self.project_data['columns'] == Property_Area))[0]

        col_count = len(self.project_data['columns'])
        test_array = np.zeros(col_count)
       
        test_array[0]=Gender
        test_array[1]=Married
        test_array[2]=Education
        test_array[3]=Self_Employed
        test_array[4]=eval(self.user_data['ApplicantIncome'])
        test_array[5]=eval(self.user_data['CoapplicantIncome'])
        test_array[6]=eval(self.user_data['LoanAmount'])
        test_array[7]=eval(self.user_data['Loan_Amount_Term'])
        test_array[8]=eval(self.user_data['Credit_History'])
        test_array[Dependents_index]=1
        test_array[Property_Area_index]=1

        Loan_Status= self.model.predict([test_array])[0]
        # return Loan_Status
        if Loan_Status==1:
            return 'Approved'
        else:
            return 'Declined'

if __name__=='__main__':
    status=LoanData()
    status


    
