#FLASK LIBRARY AND FLASK PLUGINS
from flask import request, jsonify
from flask_restful import Resource

#CUSTOM FILES
from functions.scrapers import scrape_indeed_jobs

class FindCareersResource(Resource):
	def post(self):
		'''
		This function retrieves a post request of a job title and location and returns a list of 
		jobs with that given title and in that given location.
		'''

		#Retrieve content from post request
		content = request.json
		jobs = scrape_indeed_jobs(content['title', content['location']])
		return jsonify({'data':jobs, 'status':'success'})

