from application import app
import random


@app.route('/randomFS', methods=['GET'])
def ending():

	list = ['Akira','Allegro','Anchor','Dove','Fox','Wren']
	
	return list[random.randrange(6)]