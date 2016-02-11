from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats

#@author: Ishola Babatunde
#@date: 02/08/16
#lcg uses simple linear congruential generator to create n random numbers

def init():
    global M
    M = 2048

def seed(value):
    #set seed valuegit 
	global x_i
	x_i = float(value)

# linear congruential generator   
def lcg():
    # define lcg specific parameters
	a = 1229
	c = 1
	
	global x_i
	x_i = mod(a*x_i + c, M)
	return x_i

#generate n random series using lcg
def lcg_randoms(seedValue, n):
    seed(seedValue)
    x = []
    #x.append(x_i)
    for i in range(n):
        x.append(lcg())
    return x

# extract x and y alternating points    
def split_data(data):
    x = data[::2]
    y = data[1::2]
    
    return x, y
    
# generate scaled x and y data    
def generate_data(s, N):
    series = lcg_randoms(s, N)
    [x, y] = split_data(series)
    scaled_x = [x/M for x in x]
    scaled_y = [y/M for y in y]
    return scaled_x, scaled_y

#plot
def plotxy(x, y, title):
	plt.figure(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x,y,'bo')
	plt.savefig('result/'+title)
	
	
def main():
    init()
    [x, y] = generate_data(567, 2000)
    #prints the covariance of x,y
    out = open('result/q1.txt', 'w+')
    print >>out, 'covariance of x and y \n for simple linear congruential generator:'
    print >>out, cov(x,y)
    out.close()
    plotxy(x,y,'q1-lcg')
    
if __name__ == '__main__':	
	main() 
