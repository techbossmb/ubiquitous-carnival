from numpy import *
import box_muller as boxmuller
import matplotlib.pyplot as plt
import goodness_of_fit as gof
from scipy import stats
import lorentzian

#@author: Ishola Babatunde
#@date: 03/01/2016
# tests the goodness of fit of cauchy distributed rvs

#generate cauchy distributed rvs given shape
def generate_cauchy_rvs(sample_size):
	rvs = lorentzian.generate_univariate_data(sample_size)
	return rvs

#test cauchy fit
def test_cauchy_fit(sample_size):
	rvs = generate_cauchy_rvs(sample_size)
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : stats.gamma(5).pdf(x) #cauchy was derived from gamma through the rejection method
	print 'testing cauchy distribution with '+str(sample_size)+' samples'
	gof.do_chi(rvs, number_of_bins, integrand)

def main():
	test_cauchy_fit(1000)
	print '\n'
	test_cauchy_fit(10000)

if __name__=='__main__':
	main()


