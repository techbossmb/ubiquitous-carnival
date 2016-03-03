#file helper functions
def write(string):
	file = open('result/result.txt', 'w+')
	print >>file, string
	file.close()

def append(string):
	file = open('result/result.txt', 'a')
	print >>file, string
	file.close()
