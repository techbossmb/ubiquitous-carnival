from numpy import *
import time
import matplotlib.pyplot as plt
import pylab
from scipy import stats, special
from scipy.integrate import quad

#@author: Ishola Babatunde
#@date: 02/16/16
#@ lorentzian distribution from gamma distribution

#initialize parameters of the lorentzian distribution
def initVars():
	global a0, c0, x0
	a0, c0, x0 = 1, 5, 3
	
#evaluate the gamma distribution - defined only for +ve values
def gamma_dist(x):
	n = 5
	if x <= 0:
		g_x = 0
	else:
		g_x = (x**(n-1)*exp(-x))/24
	return g_x

#evaluate lorentzian distribution
def lorentzian(x):
	f_x = (c0/(1+ (x - x0)**2)/a0)
	return f_x

#calculate the integrand, integrating from zero to +ve infinity
def integral_fx():
	maxValue, err = quad(lorentzian, 0, Inf)
	return maxValue

#calculate the g_of_z
def calculateXGivenZ(z):
	_3root1 = c0*sqrt(a0)
	return c0 + (sqrt(a0) * tan(z/_3root1))
	
#calculate mean and variance of the distribution
def calculate_stats(z):
	#calculate mean
	ev = mean(z)
	print 'Mean: ' + str(ev)
	#calculate variance
	variance = var(z)
	print 'Variance: ' + str(variance)

#added this function to produce result for hw3
def generate_univariate_data(n):
	initVars()
	A = integral_fx()
	rvs = []
	while(size(rvs) < n):
		u1 = random.uniform(0, A)
		x = calculateXGivenZ(u1)
		f_x = lorentzian(x)
		u2 = random.uniform(0, f_x)
		p_x = gamma_dist(x)
		if(u2 <= p_x):#accept
			rvs.append(x)
	return rvs

#entry point
#does the lorentzian distribution using the rejection method over the gamma distribution
def main():
	accepted = []
	initVars()
	A = integral_fx()
	print 'Area under the curve = '+ str(A)
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
	print 'rejected '+str(10000-size(accepted))+' out of 10000'
	plt.show()
	
if __name__=='__main__':
	main()

