from numpy import *
import box_muller as boxmuller
import matplotlib.pyplot as plt
import goodness_of_fit as gof
from scipy import stats

#@author: Ishola Babatunde
#@date: 03/01/2016
# tests the goodness of fit of gamma distributed rvs

#generate gamma distributed rvs given shape
def generate_gamma_rvs(shape):
	variance = stats.gamma(shape).var()
	sigma = sqrt(variance)
	sample_size = gof.get_sample_size(sigma, '99%', 0.01)
	rvs = stats.gamma(shape).rvs(size=sample_size)
	return rvs

#test gamma fit
def test_gamma_fit():
	shape = 5
	rvs = generate_gamma_rvs(shape)
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : stats.gamma(5).pdf(x)
	print 'testing gamma distribution'
	gof.do_chi(rvs, number_of_bins, integrand)

def main():
	test_gamma_fit()

if __name__=='__main__':
	main()
