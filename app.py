from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

with open ('RandomForest_stroke.pkl','rb') as f:
    model=pickle.load(f)

#by default method get
@app.route('/')   #it is use to routing path for url
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
      age=float (request.form.get('uage'))
      hypertension=float (request.form.get('uhypertension'))
      heart_disease=float (request.form.get('uheart_disease'))
      avg_glucose_level=float (request.form.get('uglucose'))
      Bmi=float (request.form.get('ubmi'))
      gender=float (request.form.get('ugender'))
      married=float (request.form.get('umarried'))
      Work_type=float (request.form.get('uwork'))
      Residency_type=float (request.form.get('uresidency'))
      Smoking_type=float (request.form.get('usmoking'))

      
      input=[[age,hypertension,heart_disease,avg_glucose_level,Bmi,gender,married,Work_type,Residency_type,Smoking_type]]
    
      predict=model.predict(input)
      print(predict)
      if predict==[0] :
        result="No Stroke"
      else:
        result="Stroke"

      return render_template('result.html', res= result)

if __name__=='__main__':
    app.run(debug=True)