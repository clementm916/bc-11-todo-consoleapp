from firebase import firebase

def synchronize(ffb_data):
	"""
	Synchronizes database to remote firebase storage
	"""
	try:
		fbase = firebase.FirebaseApplication('https://todo-823db.firebaseio.com/', None)
		mydata = ffb_data
		fbase.post('/',mydata,connection=None,params ={'print': 'pretty'},
			headers={'X_FANCY_HEADER': 'VERY FANCY'})
	except:
		return "connection error"
