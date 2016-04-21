"""
@author: Ishola Babatunde
file writer helper functions
"""
#write new content, deletes any previous result.txt file 
def write(string):
	with open('result/result.txt', 'w+') as file:
		print >>file, string #redirect print output to file
#write in append mode
def append(string):
	print string
	with open('result/result.txt', 'a') as file:
		print >>file, string #redirect print output to file

