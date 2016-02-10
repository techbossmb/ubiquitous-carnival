from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats

#@author: Ishola Babatunde
#@date: 02/08/16
#shuffled version of linear congruential generator

def initM(args=None):
    global M
    M = 2048
    if args is not None:
		M = args
		
def seed(value):
    #set seed value
	global x_i
	x_i = value

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
    series = []
    for i in range(n):
        series.append(lcg())
    return series

#shuffle n random numbers from N lcg_random numbers using T table with s = seed value
def shuffle(s, n, N):
	series = lcg_randoms(s, N+2)
	x = lag_series(series, 0, N)
	y = lag_series(series, 1, N)
	z = lag_series(series, 2, N)
	
	#needed to revert M to float
	initM(float(M)) 
	#L: table T of L values 
	L = 100
	T = []
	for j in range(L):
		t_j = (x[j+1] + (y[j+1])/M )/M
		T.append(t_j)
	#generate n random numbers	
	w = []
	for k in range(n):
		w_k = T[ z[k+1] %L ]
		T[ z[k+1]%L ] = (x[k+L+3] + (y[k+L+1])/M )/M
		w.append(w_k)
	return w
	
def lag_series(series, lag, length):
	return series[lag:length+lag]
	
# extract x and y alternating points    
def split_data(data):
    x = data[::2]
    y = data[1::2]
    return x, y
    
# generate scaled x and y data given seed value = s 
def generate_data(s, n, N):
    series = shuffle(s, n, N)
    #print series
    [x, y] = split_data(series)
    scaled_x = [x for x in x]
    scaled_y = [y for y in y]
    return scaled_x, scaled_y
    

#plot
def plotxy(x, y, title):
	plt.figure(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x,y,'bo')
	plt.savefig('result/'+title)
	
	
# entry point    
def main():
    initM()
    [x, y] = generate_data(457, 2000, 5000)
    #prints the covariance of x,y
    out = open('result/q2.txt', 'w')
    print >>out, 'covariance of x and y \n for shuffled lcg:'
    print >>out, cov(x,y)
    out.close()
    plotxy(x,y,'q2-shuffled_lcg')

if __name__ == '__main__':	
	main() 

