def readStatus():
	with open('temp/vars.txt') as file:
		status = file.readlines()[-1]
		return status


def writeStatus(stat):
	my_file = open('temp/vars.txt', "w")
	my_file.write(stat) 
	my_file.close()

def readLastOpen():
	with open('temp/read.txt') as file:
		status = file.readlines()[-1]
		try:
			return int(status)
		except:
			return status

def writeLastOpen(last):
	last =str(last)
	my_file = open('temp/read.txt', "w")
	my_file.write(last) 
	my_file.close()

