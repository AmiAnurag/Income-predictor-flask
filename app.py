# prediction function
import numpy as np
from flask import Flask,render_template,request
import pickle


app=Flask(__name__)

def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1,6)
	loaded_model = pickle.load(open("model.pkl", "rb"))
	result = loaded_model.predict(to_predict)
	print(to_predict)
	return result[0]

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(int, to_predict_list))
		result = ValuePredictor(to_predict_list)	
		if int(result)== 1:
			prediction ='Income more than 50K'
		else:
			prediction ='Income less that 50K'		
		return render_template('index.html',prediction=prediction)

if __name__=="__main__":
	app.run(debug=False)