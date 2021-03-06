from numpy import *
import goodness_of_fit as gof
from random import random
import writer

#@author: Ishola Babatunde
#@date: 02/29/2016
# tests the goodness of fit of python uniform rv

#generate python default random() uniform rvs
def generate_random_rvs():
	sigma = 1/float(12) #standard deviation ((b-a)^2)/12
	margin_error = 0.01 #for mean of 0.5
	sample_size = gof.get_sample_size(sigma, '99%', margin_error)
	rvs = empty([sample_size, 1])
	return [random() for rvs in rvs]

#test random() fit
def test_random_fit():
	rvs = generate_random_rvs()
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : 1 #pdf for uniform rv
	writer.append('testing random')
	gof.do_chi(rvs, number_of_bins, integrand)

def main():
	test_random_fit()

if __name__=='__main__':
	main()
