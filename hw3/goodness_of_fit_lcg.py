from numpy import *
import goodness_of_fit as gof
import lcg

#@author: Ishola Babatunde
#@date: 02/29/2016
# tests the goodness of fit of lcg rv

#generate linear congruential generator uniform rvs
def generate_lcg_rvs():
	sigma = 1/float(12)
	margin_error = 0.01 #chosing 0.01 for mu 0f 0.5
	sample_size = gof.get_sample_size(sigma, '99%', margin_error)
	seed = 345 # just some arbitrary value
	lcg_data = lcg.generate_univariate_data(seed, sample_size)
	return lcg_data

#test lcg fit
def test_lcg_fit():
	rvs = generate_lcg_rvs()
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : 1 #pdf for uniform rv
	print 'testing lcg'
	gof.do_chi(rvs, number_of_bins, integrand)

def main():
	test_lcg_fit()

if __name__=='__main__':
	main()
