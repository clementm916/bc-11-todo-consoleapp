def stringToList(s):
	try:
		if s[0] == '[':
			templist =[]
			for i in range(1,len(s)):
				if s[i] ==']':
					break
				templist.append(s[i])

			derlist = [joinThem(templist)]

			return derlist

		else:
			return -1
	except(TypeError):
		return -1

def joinThem(number):
    return int(''.join(str(i) for i in number))


