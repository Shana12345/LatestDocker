from application import app
import random


@app.route('/randomFS', methods=['GET'])
def beginning():

	list = ['Riley','Jordan','Angel','Spencer','Hayden','Phoenix']
	
	return list[random.randrange(6)]