from numpy import *
import random as random
import pylab

def main():
	data = [5,4,9,21,17,11,20,7,10,21,15,13,16,8]
	num_trials = 10000
	trial = [0 for x in range(num_trials)]
	var_data = var(data)
	for iTrial in range(num_trials): 
		bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
		bootstrap_var = var(bootstrap)
		trial[iTrial] = (bootstrap_var - var_data)**2
	var_error = sum(trial)/float(num_trials)
	print(var_error)

if __name__=='__main__':
	main()
