#THIRD PARTY LIBRARIES HERE
import requests

r = requests.post(
	'http://localhost:5000/api/find_careers',
	json = {
		'description' : 'I work with data and computers.'
	}
)
print(r.text)