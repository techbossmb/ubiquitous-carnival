from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from random import random

#@author: Ishola Babatunde
#@date: 02/08/16
#@random number generator uses python random() function

#generate n random series using py random()
def py_randoms(n):
	series = zeros([n,1])
	return [random() for series in series]

# extract x and y alternating points    
def split_data(data):
	x = data[::2]
	y = data[1::2]
	return x, y

# generate scaled x and y data    
def generate_data(N):
	series = py_randoms(N)
	[x, y] = split_data(series)
	return x, y

#make plot
def plotxy(x, y, title):
	plt.figure(title)
	plt.plot(x,y,'bo')
	plt.show()


# entry point    
def main():
	# generate 2000 random numbers
	N = 2000
	[x, y] = generate_data(N)
	#prints the covariance of x,y
	out = open('q3.txt', 'w')
	print >>out, 'covariance of x and y \n for py .random():'
	print >>out, cov(x,y)
	plotxy(x,y,'q3-py_random')

if __name__ == '__main__':
	main() 

