from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import random as rnd
import writer
from decimal import Decimal

#@author: Ishola Babatunde
#@date: 03/13/16

def rnd_100_walk(p):
	u = zeros([100,1])
	u = [rnd.random() for u in u]
	u = [1 if u<p else -1 for u in u]
	if sum(u) >= 70:
		p_ratio = 1/float(2*p)
		n_ratio = 1/float(2*(1-p))
		likelihood = 1;
		for u in u:
			if u == 1:
				likelihood = likelihood*p_ratio 
			else:
				likelihood = likelihood*n_ratio
		return likelihood
	else:
		return 0

def rnd_multi_walk(N):
	total = 0
	for i in range(N):
		total = total + rnd_100_walk(0.85)
	return "%.2e"%(total/float(N))

#entry point
def main():
	likelihood = rnd_multi_walk(100)
	writer.append("random walk likelihood is "+str(likelihood))

if __name__=="__main__":
	main()
