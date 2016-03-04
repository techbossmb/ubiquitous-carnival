#file helper functions

#write the 
def write(string):
	with open('result/result.txt', 'w+') as file:
		print >>file, string #redirect print output to file

def append(string):
	with open('result/result.txt', 'a') as file:
		print >>file, string #redirect print output to file
