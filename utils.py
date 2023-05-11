import pickle
import json

import numpy as np

class Credit_Card_Default():

    def __init__(self, LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
                    PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
                    BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
                    PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6) :
        self.LIMIT_BAL = LIMIT_BAL
        self.SEX = SEX
        self.EDUCATION = EDUCATION
        self.MARRIAGE = MARRIAGE
        self.AGE = AGE
        self.PAY_0 = PAY_0
        self.PAY_2 = PAY_2
        self.PAY_3 = PAY_3
        self.PAY_4 = PAY_4
        self.PAY_5 = PAY_5
        self.PAY_6 = PAY_6
        self.BILL_AMT1 = BILL_AMT1
        self.BILL_AMT2 = BILL_AMT2
        self.BILL_AMT3 = BILL_AMT3
        self.BILL_AMT4 = BILL_AMT4
        self.BILL_AMT5 = BILL_AMT5
        self.BILL_AMT6 = BILL_AMT6
        self.PAY_AMT1 = PAY_AMT1
        self.PAY_AMT2 = PAY_AMT2
        self.PAY_AMT3 = PAY_AMT3
        self.PAY_AMT4 = PAY_AMT4
        self.PAY_AMT5 = PAY_AMT5
        self.PAY_AMT6 = PAY_AMT6
        return 

    def __load_model(self): # Private Method
        # Load Model File
        with open(r'model.pkl', 'rb') as f:
            self.model = pickle.load(f)
            print('self.model >>',self.model)

        with open(r'project_data.json','r') as f:
            self.project_data = json.load( f)
            print("Project Data :",self.project_data)    

        
        
    def get_defaulter(self): # Public Method
        self.__load_model()
        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0][0] = self.LIMIT_BAL
        test_array[0][1] = self.SEX
        test_array[0][2] = self.EDUCATION
        test_array[0][3] = self.MARRIAGE
        test_array[0][4] = self.AGE
        test_array[0][5] = self.PAY_0
        test_array[0][6] = self.PAY_2
        test_array[0][7] = self.PAY_3
        test_array[0][8] = self.PAY_4
        test_array[0][9] = self.PAY_5
        test_array[0][10] = self.PAY_6
        test_array[0][11] = self.BILL_AMT1
        test_array[0][12] = self.BILL_AMT2
        test_array[0][13] = self.BILL_AMT3
        test_array[0][14] = self.BILL_AMT4
        test_array[0][15] = self.BILL_AMT5
        test_array[0][16] = self.BILL_AMT6
        test_array[0][17] = self.PAY_AMT1
        test_array[0][18] = self.PAY_AMT2
        test_array[0][19] = self.PAY_AMT3
        test_array[0][20] = self.PAY_AMT4
        test_array[0][21] = self.PAY_AMT5
        test_array[0][22] = self.PAY_AMT6


        print("Test Array is :",test_array)
       

        predicted_charges = self.model.predict(test_array)[0]
        print("Predicted Charges :", predicted_charges)
        return predicted_charges