#CUSTOM FILES
from app import app
from models import db
from models.Careers import Careers

#THIRD PARTY LIBRARIES
import pandas as pd 

#LOAD FILE INTO MEMORY
df = pd.read_csv('seeds/data/soc.csv', encoding = 'cp1252')

#PUT DATA INTO DATABASE
with app.app_context():
	for index, row in df.iterrows():
		new_career = Careers(
			index, 
			row['SOC Title'],
			row['SOC Definition']
		)
		db.session.add(new_career)
	db.session.commit()

print("Completed")