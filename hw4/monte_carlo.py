from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import random as random
import writer

def run_problem1(sample_size):
	u = zeros([sample_size,1])
	u = [random.random() for u in u]
	f_x = [-1 * log(1-u) for u in u]
	g_x = [cos(f_x) for f_x in f_x]
	mu = mean(g_x)
	#cf1 = (mu - 0.5)**2
	#cf2 = var(g_x)/(0.01*sample_size)
	#print cf1, cf2
	writer.append("problem 1 mean is "+str(mu))

def run_problem2(sample_size):
	u = zeros([sample_size, 1])
	u = [random.random() for u in u]
	#u = [stats.norm.rvs() for u in u] #not sure whether to use normal or uniform rv
	f_x = [arccos((1-u)-1/float(2*pi)) for u in u]
	#f_x = [arccos(2*pi*(1-u)-1) for u in u] #not sure about the equation either - arccos evaluates to nan i.e., undefined
	g_x = [2*pi*((1+cos(f_x))**(-2/float(3))) for f_x in f_x]
	mu = mean(g_x)
	writer.append("problem 2 mean is "+str(mu))

def main():
	run_problem1(10000)
	run_problem2(10000)

if __name__=="__main__":
	main()

