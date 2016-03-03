#file helper functions
def write(string):
	with open('result/result.txt', 'w+') as file:
		print >>file, string

def append(string):
	with open('result/result.txt', 'a') as file:
		print >>file, string
