from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import unidecode



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])



def predict():
	def preprocess(names_df, train=True):
		# Lowercase
		names_df['name'] = names_df['name'].str.lower()

		# if name provided has more than 1 word, take 1st word
		names_df['name'] = names_df['name'].apply(lambda x:x.split()[0])

	    # Remove accent
		names_df['name'] = names_df['name'].apply(lambda x:unidecode.unidecode(x))
	    
	    # Remove non-alphabet characters
		names_df['name'] = [
	        "".join([
	            char
	            for char in name
	            if char.isalpha()==True
	        ])
	        for name in names_df['name']
	    ]
	    
	    # drop duplicate rows
		names_df = names_df.drop_duplicates().reset_index(drop=True)
	    
	    # drop NaN
		names_df = names_df.dropna().reset_index(drop=True)
	    
		
	    # Split individual characters
		names_df['name'] = [list(name) for name in names_df['name']]

	    # Step 3: Pad names with spaces to make all names same length
		name_length = 20
		names_df['name'] = [
	        (name + [' ']*name_length)[:name_length] 
	        for name in names_df['name']
	    ]

	    # Encode Characters to Numbers
		names_df['name'] = [
	        [
	            max(0.0, ord(char)-96.0) 
	            for char in name
	        ]
	        for name in names_df['name']
	    ]
	    
	    # Encode Gender to Numbers
		if train:
	        
			names_df['gender'] = [
	            0 if gender=='F' else 1
	            for gender in names_df['gender']
	        ]
	    
		return names_df

	# load model
	pred_model = load_model('models/BiLSTM_GC.h5')

	# Receives the input query from form
	if request.method == 'POST':

		# Input names
		namequery = request.form['namequery']
		names = [namequery]

		# Convert to dataframe
		pred_df = pd.DataFrame({'name': names})

		# Preprocess
		pred_df = preprocess(pred_df, train=False)

		# Predictions
		result = pred_model.predict(np.asarray(
		    pred_df['name'].values.tolist())).squeeze(axis=1)

	return render_template('results.html',prediction = int(round(result[0],0)), name = namequery.upper())

if __name__ == '__main__':
	app.run(debug=True)