from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from preprocess import preprocess

# Declare a Flask app
app = Flask(__name__)


# If a form is submitted from website.html, 
# make prediction with LSTM 
# and return prediction to website
@app.route('/', methods=['GET', 'POST'])
def main():
    
  # If a form is submitted (POST request from HTML)
  if request.method == "POST":
      
    # load trained classifier model
    #clf = joblib.load("clf.pkl")
    loaded_lstm = load_model('models/lstm.h5')
    
    # Get values through input bars
    name = request.form.get("name")
    
    # Put input to dataframe
    names_genders = pd.DataFrame({'name': [name]})
    
    # Preprocess
    names_genders = preprocess(names_genders, train=False)
    
    # Prediction
    result = loaded_lstm.predict(np.asarray(names_genders['name'].values.tolist())).squeeze(axis=1)[0]
      
    # Format prediction
    if result> 0.5:
      prediction = 'LSTM says ' + name + ' is ' + str(round(result*100,2)) + '% Male!'
    else:
      prediction = 'LSTM says ' + name + ' is ' + str(round(100-result*100,2)) + '% Female!'
      
  else:
    prediction = ""
  
  # send to HTML, syntax: name_in_HTML = name_in_Python
  return render_template("website.html", output = prediction)

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
