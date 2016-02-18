from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats

#@author: Ishola Babatund
#@date: 02/16/16
#@ box-muller transformation of a uniform to normal distribution

#generate uniform dist. data
def gen_uniform_rv(n):
	u1 = random.rand(n)
	u2 = random.rand(n)
	return u1, u2

#generate normal dist. data	
def gen_normal_rv(n):
	[u1, u2] = gen_uniform_rv(n)
	[z1, z2] = transform(u1, u2)
	return z1, z2

#use box-muller transformation to convert uniform to normal dist.	
def transform(u1, u2):
	z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
	z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
	return z1, z2

#plot and save histogram to file
#note:ensure you mkdir before trying to save plot in result folder
def plot_hist(data, title):
	plt.figure(title)
	plt.hist(data)
	plt.savefig('result/'+title)
	plt.show()

def calculate_stats(z1, z2):
	z = z1 + z2
	#calculate mean
	ev = mean(z)
	print 'Mean: ' + str(ev)
	#calculate variance
	variance = var(z)
	print 'Variance: ' + str(variance)

def main():
	[z1, z2] = gen_normal_rv(10000)
	plot_hist(z1, 'z1')
	plot_hist(z2, 'z2')
	calculate_stats(z1, z2)

if __name__=='__main__':
	main()
