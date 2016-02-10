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
    series = empty([n,1])
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

#plot
def plotxy(x, y, title):
	plt.figure(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x,y,'bo')
	plt.savefig('result/'+title)
	
	
# entry point    
def main():
    [x, y] = generate_data(2000)
    #prints the covariance of x,y
    out = open('result/q3.txt', 'w')
    print >>out, 'covariance of x and y \n for py .random():'
    print >>out, cov(x,y)
    out.close()
    plotxy(x,y,'q3-py_random')
    
if __name__ =='__main__':	
	main() 

