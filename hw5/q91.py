from numpy import *;
import random as random

def main():
	trials = 1000
	var_control = []
	var_anti = []
	var_star = []
	estimator = lambda u: exp(u**2) * (1+exp(1-(2*u)))/2.0

	for i in range(trials):
		rands = [random.random() for i in range(100)]
		x = exp([r**2 for r in rands])
		covxy = cov(x,rands)
		cstar = -covxy[1,0]/float(var(rands))
		estimate = x + cstar*(rands - mean(rands))
		var_control.append(var(estimate))
		var_anti.append(var([estimator(r) for r in rands]))
		var_star.append(cstar)

	print('cstar: ', mean(cstar))
	print('var(x,y): ', mean(var_anti))
	print('var(z): ', mean(var_control))

if __name__=='__main__':
	main()
