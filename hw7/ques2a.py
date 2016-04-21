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

def huen_soln(delta_t):
	time = linspace(0, 1, 1/float(delta_t))
	sdt = sqrt(delta_t)
	x = zeros((int(1/float(delta_t)),1))
	x[0] = 1 #x0
	a=1.5
	b=0.1
	for i in range(1, int(1/float(delta_t))):
		x_n = x[i-1]
		w_t = random.normal(0, delta_t)*sdt
		x_tilde = x_n+(a*x_n)* delta_t + (b*x_n) * w_t
		#huen expands on euler soln
		x_t=x_n+(0.5)*((a*x_n)+(a*x_tilde)) * delta_t + (
				(0.5)*((b*x_n)+(b*x_tilde))) * w_t
		x[i] = x_t
	return x

def run():
	dts = [2**-3, 2**-4, 2**-5, 2**-6]
	n = 100
	
	#err = zeros((size(dts),1))
	errs1 = []
	errs2 = []
	for j in range(size(dts)):
		sum0,sum1,sum2 = 0,0,0
		z0 = []
		z1 = []
		err = []
		for i in range(100):
			#s0 is the array returned by the euler algorithm
			s0 = eulersde(1,0,1,dts[j],1.5,0.1)
			sum0 = sum0 + s0 #I'm not sure that we really expect
			#s1 is the array returned by the exact algorithm
			s1 = exactsde(1,0,1,dts[j],1.5,0.1)
			sum1 = sum1 + s1 #not sure what is being done here
			s2 = huen_soln(dts[j])
			sum2 = sum2 + s2
		z0 = (sum0/float(n))
		z1 = (sum1/float(n))
		z2 = (sum2/float(n))
		#print z0
		zt0 = z0
		zt1 = z1
		zt2 = z2
		err1 = [z1-z0 for z1,z0 in zip(z1,z0)]
		err2 = [z1-z2 for z1,z2 in zip(z1,z2)]
		#plotxyz(linspace(0,1,1/dts[j]), zt0, zt1, 'b','r', 'dt=2^-'+str(j+3), 0)
		#plotxyz(linspace(0,1,1/dts[j]), zt0, zt2, 'b','r', 'dt=2^-'+str(j+3), 0)
		#plotxy(linspace(0,1,1/dts[j]), err, 'r', 'dt=2^-'+str(j+3), 0)
		errs1.append(mean(err1))
		errs2.append(mean(err2))
	plotxyz(dts, errs1, errs2, 'b','r', 'b-euler vs r-heun', 1)
	#plotxy(dts, errs2, 'r', 'heun', 1)

	#errs = [z1 - z0 for z1,z0 in zip(z1,z0)]
	#plotxy(dts, z0)
def plotxy(x,y, color, title, show):
	plt.figure('q2a - err'+title)
	plt.xlabel('delta t')
	plt.ylabel('error')
	plt.plot(x,y, color+'-o')
	plt.savefig('result/err'+title)
	if show==1:
		plt.show()
	
def plotxyz(x,y,z, color_y, color_z,title, show):
	plt.figure('q2a - '+title)
	plt.xlabel('delta t')
	plt.ylabel('expected value')
	plt.plot(x,y, color_y+'-o')
	plt.plot(x,z, color_z+'-o')
	plt.savefig('result/'+title)
	if show==1:
		plt.show()
				
 
if __name__=='__main__':
	main()
