#THIRD PARTY LIBRARIES 
import requests
from bs4 import BeautifulSoup


def scrape_indeed_jobs(job_title, location):
	'''
	This function takes in a job title and a location, then returns a list
	of jobs in that field and area from Indeed.com
	'''

	#Replace spaces with plus signs for URL 
	job_title = job_title.replace(' ','+')
	location = location.replace(' ','+')

	#Scrape postings from Indeed
	url = 'https://www.indeed.com/jobs?q={}&l={}&start=10'.format(job_title, location)
	r = requests.get(url)

	#Parse Indeed web page
	soup = BeautifulSoup(r.text, 'html.parser')
	jobs = []

	for div in soup.find_all(name = 'div', attrs = {'class':'job_seen_beacon'}):
		job_data = {}

		#Scraoe job title
		indeed_job_title = div.find(name='h2', attrs={'class':'jobTitle'})
		job_data['title'] = indeed_job_title.get_text()

		#Scrape job location 
		indeed_job_location = div.find('div', attrs={'class':'company_location'})
		if indeed_job_location != None:
			job_data['company'] = indeed_job_location.get_text()
		else:
			job_data['company'] = 'Unknown Company'

		#Scrape salary snippet
		indeed_salary_snippet = div.find('span', attrs={'class':'salary-snippet'})
		if indeed_salary_snippet != None:
			job_data['salary'] = indeed_salary_snippet.get_text()
		else:
			job_data['salary'] = 'Unknown Salary Band'
		

		jobs.append(job_data)
	return jobs

if __name__ == "__main__":
	print(scrape_indeed_jobs('Data Scientist','Houston'))