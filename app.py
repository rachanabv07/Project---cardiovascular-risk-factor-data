from flask import Flask, render_template, request
import pickle
import sklearn


app = Flask(__name__)
model = pickle.load(open('model_predict.pkl', 'rb'))
print(type(model))

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction_result = ""
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(1 if request.form['sex'] == 'Male' else 0)
        is_smoking = int(1 if request.form['is_smoking'] == 'YES' else 0)
        cigsPerDay = int(request.form['cigsPerDay'])
        BPMeds = int(1 if request.form['BPMeds'] == 'YES' else 0)
        PrevalentStroke = int(1 if request.form['PrevalentStroke'] == 'YES' else 0)
        PrevalentHyp = int(1 if request.form['PrevalentHyp'] == 'YES' else 0)
        Diabetes = int(1 if request.form['Diabetes'] == 'YES' else 0)
        totChol = int(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = int(request.form['heartRate'])
        glucose = int(request.form['glucose'])
        
    
        
        # Make predictions using model 
        prediction = model.predict([[age, sex, is_smoking, cigsPerDay, BPMeds, PrevalentStroke, PrevalentHyp, Diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])
        output = prediction[0]
        
        # Modify the message based on model's output
        if output == 1:
            prediction_result = "Possible future risk of Coronary Heart Disease detected. Please consult a healthcare professional for further evaluation and guidance."
        else:
            prediction_result = "Good news! Your current assessment suggests no foreseeable risk of Coronary Heart Disease. Keep up the healthy habits and lifestyle."
    
    return render_template('text.html', prediction_result=prediction_result)



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="4100")
