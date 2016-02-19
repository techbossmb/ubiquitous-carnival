from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats, special
from scipy.integrate import quad

#@author: Ishola Babatunde
#@date: 02/16/16
#@ lorentzian distribution from gamma distribution

def initVars():
	global a0, c0, x0
	a0, c0, x0 = 1, 3, 3
	
def gamma_dist(x):
	n = 5
	if x <= 0:
		g_x = 0
	else:
		g_x = (x**(n-1)*exp(-x))/24
	return g_x

def lorentzian(x):
	f_x = (c0/(1+ (x - x0)**2)/a0)
	return f_x

def integral_fx():
	maxValue, err = quad(lorentzian, 0, Inf)
	return maxValue

def calculateXGivenZ(z):
	_3root1 = c0*sqrt(a0)
	return c0 + (sqrt(a0) * tan(z/_3root1))
	
def calculate_stats(z):
	#calculate mean
	ev = mean(z)
	print 'Mean: ' + str(ev)
	#calculate variance
	variance = var(z)
	print 'Variance: ' + str(variance)
	
def main():
	accepted = []
	initVars()
	A = integral_fx()
	print 'Area under the curve = '+A
	for i in range(10000):
		u1 = random.uniform(0, A)
		x = calculateXGivenZ(u1)
		f_x = lorentzian(x)
		u2 = random.uniform(0, f_x)
		p_x = gamma_dist(x)
		if(u2 <= p_x):#accept
			accepted.append(x)
	plt.figure('Lorentzian Distribution from Rejection Method')
	plt.hist(accepted, 50)
	plt.savefig('result/lorentzian')
	calculate_stats(accepted)
	print 'accepted '+str(size(accepted))+' out of 10000'
	plt.show()
git o
if __name__=='__main__':
	main()

