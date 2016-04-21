from numpy import *
import matplotlib.pyplot as plt
import pylab

def main():
	run()

def eulersde(x_0, t_0, t_f, dt, f, g):
	t = linspace(0,1,1/dt)
	n = t.shape[0]
	sqrt_dt = sqrt(dt)
	x_t = zeros((n,1))
	x_t[0] = x_0
	for i in range(n-1):
		rand_var = dt*random.randn()
		x_t[i+1] = x_t[i] + f*x_t[i]*dt + g*x_t[i]*rand_var*sqrt_dt
	return x_t

def exactsde(x_0, t_0, t_f, dt, a, b):
	t = linspace(0,1,1/dt)
	n = t.shape[0]
	sqrt_dt = sqrt(dt)
	b_t = zeros((n,1))
	n_t = zeros((n,1))
	n_t[0] = x_0
	for i in range(n-1):
		b_t[i+1] = b_t[i] + sqrt_dt*dt*random.randn()
		n_t[i+1] = n_t[0]*exp((a-0.5*b**2)*t[i] + b*b_t[i+1])
	return n_t

def run():
	dts = [2**-3, 2**-4, 2**-5, 2**-6]
	n = 100
	z0 = []
	z1 = []
	for j in range(size(dts)):
		sum0,sum1 = 0,0
		for i in range(n):
			#s0 is the array returned by the euler algorithm
			s0 = eulersde(1,0,1,dts[j],1.5,0.1)
			sum0 = sum0 + s0 #I'm not sure that we really expect
			#s1 is the array returned by the exact algorithm
			s1 = exactsde(1,0,1,dts[j],1.5,0.1)
			sum1 = sum1 + s1 #not sure what is being done here
		z0.append(sum0/float(n))
		z1.append(sum1/float(n))
	errs = [z1 - z0 for z1,z0 in zip(z1,z0)]
	plotxy(dts, errs)

def plotxy(x,y):
	plt.figure('q2a')
	plt.xlabel('delta t')
	plt.ylabel('error')
	plt.plot(x,y,'bo')
	plt.savefig('result/figq2a')
	plt.show()
				
 
if __name__=='__main__':
	main()
