from flask import Flask, render_template, jsonify, request
from utils import Credit_Card_Default

import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    try:
        if request.method == 'POST':
            data = request.form.get


            print("User Data is :",data)
            LIMIT_BAL = int(data('LIMIT_BAL'))
            SEX = int(data('SEX'))
            EDUCATION = int(data('EDUCATION'))
            MARRIAGE = int(data('MARRIAGE'))
            AGE = int(data('AGE'))
            PAY_0 = eval(data('PAY_0'))
            PAY_2 = eval(data('PAY_2'))
            PAY_3 = eval(data('PAY_3'))
            PAY_4 = eval(data('PAY_4'))
            PAY_5 = eval(data('PAY_5'))
            PAY_6 = eval(data('PAY_6'))
            BILL_AMT1 = eval(data('BILL_AMT1'))
            BILL_AMT2 = eval(data('BILL_AMT2'))
            BILL_AMT3 = eval(data('BILL_AMT3'))
            BILL_AMT4 = eval(data('BILL_AMT4'))
            BILL_AMT5 = eval(data('BILL_AMT5'))
            BILL_AMT6 = eval(data('BILL_AMT6'))
            PAY_AMT1 = eval(data('PAY_AMT1'))
            PAY_AMT2 = eval(data('PAY_AMT2'))
            PAY_AMT3 = eval(data('PAY_AMT3'))
            PAY_AMT4 = eval(data('PAY_AMT4'))
            PAY_AMT5 = eval(data('PAY_AMT5'))
            PAY_AMT6 = eval(data('PAY_AMT6'))
            
            cc_defualt = Credit_Card_Default(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
                                            PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
                                            BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
                                            PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6)
            defaults = cc_defualt.get_defaulter()

            if defaults == 0:
                return render_template("index.html", prediction_text = "Next Month Defaulter")
            else:
                return render_template("index.html", prediction_text = "Next Month is Not Defaulter")

        else:
            data = request.args.get

            print("User Data is :",data)
            LIMIT_BAL = int(data('LIMIT_BAL'))
            SEX = int(data('SEX'))
            EDUCATION = int(data('EDUCATION'))
            MARRIAGE = int(data('MARRIAGE'))
            AGE = int(data('AGE'))
            PAY_0 = eval(data('PAY_0'))
            PAY_2 = eval(data('PAY_2'))
            PAY_3 = eval(data('PAY_3'))
            PAY_4 = eval(data('PAY_4'))
            PAY_5 = eval(data('PAY_5'))
            PAY_6 = eval(data('PAY_6'))
            BILL_AMT1 = eval(data('BILL_AMT1'))
            BILL_AMT2 = eval(data('BILL_AMT2'))
            BILL_AMT3 = eval(data('BILL_AMT3'))
            BILL_AMT4 = eval(data('BILL_AMT4'))
            BILL_AMT5 = eval(data('BILL_AMT5'))
            BILL_AMT6 = eval(data('BILL_AMT6'))
            PAY_AMT1 = eval(data('PAY_AMT1'))
            PAY_AMT2 = eval(data('PAY_AMT2'))
            PAY_AMT3 = eval(data('PAY_AMT3'))
            PAY_AMT4 = eval(data('PAY_AMT4'))
            PAY_AMT5 = eval(data('PAY_AMT5'))
            PAY_AMT6 = eval(data('PAY_AMT6'))

            cc_defualt = Credit_Card_Default(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
                                            PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
                                            BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
                                            PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6)
            defaults = cc_defualt.get_defaulter()

            
            if defaults == 0:
                return render_template("index.html", prediction_text = "Is Defaulter")
            else:
                return render_template("index.html", prediction_text = "Not Defaulter")

        
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5004,debug=True)