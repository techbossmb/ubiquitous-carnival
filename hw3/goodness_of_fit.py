from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import writer

"""
@author: Ishola Babatunde
@date: 02/29/2016
goodness_of_fit does chi-squared goodness of fit
	this class defines helper functions needed to 
		calculate and compare estimated chiquare to the expected chisquare, 
		estimate the number of samples to generate a random distribution within the confidence interval, and
		calculate the statistics of the rvs i.e., the mean and variance
"""

"""
maps confidence interval to zscore
@args: CI - confidence interval
@return: zscore
"""
def zmap(CI):
	ci_map = {'99%':2.576, '95%':1.96, '90%':1.645} 
	return ci_map[CI]

"""
calculates the number of sample given the statistics of the expected distribution
@args: std_dev - expected standard deviation of the distribution 
	 a quick wiki search will reveal what the standard deviation should be for a given distribution type
	CI - confidence interval 
	ME - margin error - specifies how maximum allowable deviation from the mean 
	 generated rvs mean should be in the range of mean +/- ME
@return: number of samples
"""
def get_sample_size(std_dev, CI, ME):
	zscore = zmap(CI)
	n = (zscore * std_dev / float(ME))**2
	return int(n)

"""
actually do chi-square test
compares actual vs. expected chisquare,
 accepts or rejects the null hypothesis, and
  calculate the statistics of the rvs
@args: rvs - generated rvs
	number_of_bins - tells the chisquare calculator how to divide the bins
	integrand - pdf of the distribution
@return: null - only performs action and output to file
"""
def do_chi(rvs, number_of_bins, integrand):
	actual_chisquare = calculate_chisquare(rvs, number_of_bins, integrand);
	expected_chiquare = stats.chi2.ppf(.99, number_of_bins-1)
	compare_chisquare(actual_chisquare, expected_chiquare)
	calculate_stats(rvs)

"""
calculates expected chi square 
@args: rvs - generated random variables
	number_of_bins
	integrand - pdf of the distribution
@return: chisquare
"""
def calculate_chisquare(rvs, number_of_bins, integrand):
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

"""
compare expected and actual chi square and reject or accept hypothesis
saves output to file
@args: actual (chisquare)
	expected (chisquare)
@return: null, prints output to file using writer 
"""
def compare_chisquare(actual, expected):
	writer.append('chisquared - actual: '+str(actual)+' expected: '+ str(expected))
	if actual <= expected:
		writer.append('Accept null hypothesis i.e., good fit')
	else:
		writer.append('Reject null hypothesis i.e., bad fit')

"""
calcualte mean and variance of random distribution
saves output to file
@args: rvs - generated random distribution
@return: null, prints output to file
"""
def calculate_stats(rvs):
	writer.append('mean: '+str(mean(rvs))+' variance: '+str(var(rvs)))
