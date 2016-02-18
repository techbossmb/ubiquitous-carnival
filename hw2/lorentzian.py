from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats, special
from scipy.integrate import quad

#@author: Ishola Babatunde
#@date: 02/16/16
#@ lorentzian distribution from gamma distribution

def gamma_dist(x):
	n = 5
	if x <= 0:
		g_x = 0
	else:
		g_x = (x**(n-1)*exp(-x))/24
	return g_x

def lorentzian(x):
	a0, c0, x0, = 0.2, 3, 0
	f_x = (c0/(1+ (x - x0)**2)/a0)
	return f_x

def integral_fx():
	maxValue, err = quad(lorentzian, 0, Inf)
	return maxValue

def bigFofX(x):
	F_x = 3*sqrt(2)*arctan(x/sqrt(2))
	return F_x

def calculateX():
	I = integral_fx()
	_3root2 = 3*sqrt(2)
	return sqrt(2) * tan(I/_3root2)
	
def calculateXGivenZ(z):
	_3root2 = 3*sqrt(2)
	return sqrt(2) * tan(z/_3root2)
	
def calculate_stats(z):
	#calculate mean
	ev = mean(z)
	print 'Mean: ' + str(ev)
	#calculate variance
	variance = var(z)
	print 'Variance: ' + str(variance)
	
def main():
	accepted = []
	for i in range(10000):
		A = integral_fx()
		u1 = random.uniform(0, A)
		x = calculateXGivenZ(u1)
		f_x = lorentzian(x)
		u2 = random.uniform(0, f_x)
		p_x = gamma_dist(x)
		if(u2 <= p_x):#accept
			accepted.append(x)
	plt.figure(1)
	plt.hist(accepted)
	plt.savefig('result/lorentzian')
	calculate_stats(accepted)
	print 'accepted '+str(size(accepted))+' out of 10000'
	plt.show()

if __name__=='__main__':
	main()

