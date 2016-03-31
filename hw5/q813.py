from numpy import *
import random as random
import pylab

def main():
	data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
	avg = mean(data)
	a=-5
	b=5
	num_trials=1000
	trial=[]

	for iTrial in range(num_trials): 
		bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
		trial.append(mean(bootstrap))

	difference=[(x-avg) for x in trial]
	prob=[a < x < b for x in difference]
	print('total probability: ', prob.count(True)/float(len(prob)))

if __name__=='__main__':
	main()
