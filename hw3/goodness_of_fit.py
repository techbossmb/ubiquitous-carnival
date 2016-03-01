from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
from random import random
import lcg

#maps confidence interval to zscore
def zmap(CI):
	ci_map = {'99%':2.576, '95%':1.96, '90%':1.645} 
	return ci_map[CI]

#calculates the number of sample given the statistics of the expected distribution
def get_sample_size(std_dev, CI, ME):
	zscore = zmap(CI)
	n = (zscore * std_dev / float(ME))**2
	return int(n)

#generate linear congruential generator uniform rvs
def generate_lcg_rvs():
	sigma = 1/float(12)
	sample_size = get_sample_size(sigma, '99%', 0.01)
	seed = 345 # just some arbitrary value
	lcg_data = lcg.generate_univariate_data(seed, sample_size)
	return lcg_data

#generate python default random() uniform rvs
def generate_random_rvs():
	sigma = 1/float(12)
	sample_size = get_sample_size(sigma, '99%', 0.01)
	rvs = empty([sample_size, 1])
	return [random() for rvs in rvs]

#test lcg fit
def test_lcg_fit():
	rvs = generate_lcg_rvs()
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : 1
	print 'testing lcg'
	do_chi(rvs, number_of_bins, integrand)

#test random() fit
def test_random_fit():
	rvs = generate_random_rvs()
	number_of_bins = int(1.88 * size(rvs) ** (2/5.0))
	integrand = lambda x : 1
	print 'testing random'
	do_chi(rvs, number_of_bins, integrand)

#evaluate chi-squared
def do_chi(rvs, number_of_bins, integrand):
	actual_chisquare = chisquare_test(rvs, number_of_bins, integrand);
	expected_chiquare = stats.chi2.ppf(.99, number_of_bins-1)
	compare_chisquare(actual_chisquare, expected_chiquare)
	calculate_stats(rvs)

# calculate expected chi square 
def chisquare_test(rvs, number_of_bins, integrand):
	sorted_data = sort(rvs)      
	bin_ends=linspace(0,1,number_of_bins+1) #setp up bin boundaries
	count=zeros(number_of_bins)
	expected_counts=zeros(number_of_bins)
	p=zeros(number_of_bins)
	for k in range(number_of_bins):
		temp=where((sorted_data > bin_ends[k]) & (sorted_data < bin_ends[k+1])) #gives indices of rvs that fall w/in each bin
		count[k]= size(temp) #counts indices
		p[k], err=quad(integrand,bin_ends[k],bin_ends[k+1]) #calculates probabily of rv falling w/in each bin
	n = len(rvs)
	for k in range(number_of_bins):
		expected_counts[k] =n * p[k]
	#find the chisquared value for our count
	chi_squared, pvalue = stats.chisquare(count, expected_counts)
	return chi_squared

#compare expected and actual chi square and reject or accept hypothesis
def compare_chisquare(actual, expected):
	print actual, expected
	if actual > expected:
		print 'Reject independence hypothesis i.e good fit'
	else:
		print 'Accept independence hypothesis i.e. bad fit'

#calcualte mean and variance of random distribution
def calculate_stats(rvs):
	print 'mean: '+str(mean(rvs))+' variance: '+str(var(rvs))

#entry point 
def main():
	test_lcg_fit() #test the goodness of fit for lcg generator
	test_random_fit() # test gooness of fit for random generator

if __name__=='__main__':
	main()
