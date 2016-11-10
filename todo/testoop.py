class clement(object):
	is_asleep=None
	def __init__(self,name):
		self.name = name


cl = clement("Clement")



print cl.name
clement.is_asleep = True
print cl.is_asleep


def printtuon(k):
	print k.is_asleep
clement.is_asleep =False
printtuon(cl)


l =clement("Matundu")

print l.is_asleep