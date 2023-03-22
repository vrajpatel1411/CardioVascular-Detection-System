from flask import Flask,render_template,request

import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)

model=pickle.load(open('model.pkl',"rb"))


@app.get("/")
def Home():
    return render_template('index.html',result="")

@app.post("/predict")
def predict():
    print(request.form.get('age'))
    age=int(request.form.get('age'))
    gender = int(request.form.get('gender'))
    height = int(request.form.get('height'))
    weight = int(request.form.get('weight'))
    ap_hi = int(request.form.get('ap_hi'))
    ap_lo = int(request.form.get('ap_li'))
    Cholestrol = int(request.form.get('cholestrol'))
    gluc = int(request.form.get('gluc'))
    sh = int(request.form.get('sh'))
    active = int(request.form.get('active'))
    alcohol=int(request.form.get('alcohol'))
    bmi= weight/((height*height)/100)
    data=[age,gender,bmi,ap_hi,ap_lo,Cholestrol,gluc,sh,alcohol,active]
    data=[np.array(data)]
    columns=['age','gender','BMI','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']
    data=pd.DataFrame(data,columns=columns)
    predict=model.predict(data)
    result=""
    if predict==1:
        result="Yes, their are more chances of getting cardiovascular disease in feature"
    else :
        result="You are healthy"
    return render_template('index.html',result=result)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
