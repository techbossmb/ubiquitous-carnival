from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import lcg

#@author: Ishola Babatunde
#@ques: determine the number of samples need to achieve a 99% CI for LCG generated rv

# initialize CI=>zscore map
def initMap():
	global ci_map
	ci_map = {'99%':2.576, '95%':1.96, '90%':1.645} 
	
#generate uniform rv from linear congruential generator
#args: n = number of random variables to generate
def do_lcg(n):
	lcg.init()
	rv = lcg.generate_univariate_data(345, n)
	return rv


#returns the sample size for need to achieve a given confidence interval
def get_sample_size(margin_error, confidence_interval, expected_value):
	initMap()
	z_score = ci_map[confidence_interval]
	#ME = zScore * \sqrt{\frac{EV(1-EV)}{n}}
	#make n the subject of the formula in the equation above to derive the equation for sample_size
	sample_size = (expected_value * (1 - expected_value))/((margin_error/z_score)**2)
	return sample_size


def calculata_stats(rv):
	return mean(rv), var(rv)


#def goodness_of_fit_uniform_rv(rv, ev):
#	ev_list = ev*ones(size(rv))
#	[xsquare, p_value] = stats.chisquare(rv, f_exp=ev_list)
#	return xsquare, p_value


def plot_hist(data):
	title = 'lcg_generated_uniform rv'
	plt.figure(title)
	plt.hist(data)
	plt.savefig('result/'+title)
	plt.show()

# x squared goodness of fit test using chi-square
def testing_chi(rvs, number_of_bins, integrand):
	sorted_data = sort(rvs)
	number_of_bins=10;        
	bin_ends=linspace(0,1,number_of_bins+1) #setp up bin boundaries
	count=zeros(number_of_bins)
	p=zeros(number_of_bins)
	for k in range(number_of_bins):
		temp=where((sorted_data > bin_ends[k]) & (sorted_data < bin_ends[k+1])) #gives indices of rvs that fall w/in each bin
		count[k]=size(temp) #counts indices
		p[k], err=quad(integrand,bin_ends[k],bin_ends[k+1]) #calculates probabily of rv falling w/in each bin
	n = len(rvs)
	expected_counts = [ n * p[k] for k in range(bins) ]
    #find the chisquared value for our count
    chi_squared, pvalue = scipy.stats.chisquare(count, expected_counts)
    return chi_squared


#test lcg goodness of fit
def test_lcg():
	margin_error, confidence_interval, expected_value = 0.01, '99%', 0.5
	sample_size = get_sample_size(margin_error, confidence_interval, expected_value)
	uniform_rv = do_lcg(int(sample_size))
	number_of_bins = 10
	integrand = lambda x : 1
	actual = testing_chi(uniform_rv, number_of_bins, integrand)
	expected = stats.chi2.ppf(.99, number_of_bins-1)
	#evaluate_results(actual, expected)

#entry point
def main():
	test_lcg()
	#[mu, sigma] = calculata_stats(uniform_rv)
	#print mu, sigma
	#[xsquare, p_value] = goodness_of_fit_uniform_rv(uniform_rv, expected_value)
	#print xsquare, p_value
	#plot_hist(uniform_rv)

if __name__=='__main__':
	main()
