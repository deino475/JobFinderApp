#FLASK LIBRARY AND FLASK PLUGINS
from flask import request, jsonify
from flask_restful import Resource

#CUSTOM FILES
from models import db 
from models.Careers import Careers

#Additional libraries 
from tensorflow import keras
import numpy as np 

class FindCareersResource(Resource):
	def post(self):
		'''
		This function retrieves a post request of a job description and then 
		calculates the probability that a given career matches with the description 
		provided.
		'''

		#Retrieve content from post request
		content = request.json

		#Fetch list of careers
		soc_careers = Careers.query.all()

		#Load keras model here
		keras_model = keras.models.load_model('keras_model')

		#Create a list that stores careers and their probabilities
		career_probs_list = []

		#Calculate the probabilities and store in list
		for soc_career in soc_careers:
			test_job_desc = np.array([content['description']])
			test_soc_desc = np.array([soc_career.description])

			prob = keras_model.predict([test_job_desc,test_soc_desc])
			career_probs_list.append({
				'name' : soc_career.name,
				'description': soc_career.description,
				'match' : prob.tolist()[0]
			})

		#Return top five careers
		sorted_careers = sorted(career_probs_list, key = lambda x: x['match'], reverse = True)
		return jsonify({'status':'success','data':sorted_careers[0:5]})