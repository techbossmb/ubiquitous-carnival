from numpy import *
import box_muller as boxmuller
import matplotlib.pyplot as plt
import goodness_of_fit as gof
from scipy import stats
import writer

#@author: Ishola Babatunde
#@date: 03/01/2016
# tests the goodness of fit of box-muller genereated normal rv

#generate box muller rvs given variance
def generate_muller_rvs(variance):
	sigma = sqrt(variance)
	margin_error = 0.02 #for normal distribution
	sample_size = gof.get_sample_size(sigma, '99%', margin_error)
	rvs = boxmuller.generate_univariate_data(sample_size, variance)
	return rvs

#test box-muller fit
def test_muller_fit():
	variance = 0.1 # given in the ques
	rvs = generate_muller_rvs(variance)
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : stats.norm.pdf(x, scale=variance)
	writer.append('testing box-muller')
	gof.do_chi(rvs, number_of_bins, integrand)

def main():
	test_muller_fit()

if __name__=='__main__':
	main()
