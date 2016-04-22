from numpy import * 
import matplotlib.pyplot as plt
import pylab
'''
@author: Ishola Babtunde
'''
#exact solution
def exactsde(x_0, t_0, t_f, dt, a, b):
	t = linspace(t_0,t_f,1/dt)
	n = t.shape[0]
	sqrt_dt = sqrt(dt)
	b_t = zeros((n))
	n_t = zeros((n))
	n_t[0] = x_0
	n_t_list = []
	n_t_list.append(x_0)
	for i in range(int(1/dt)-1):
		b_t[i+1] = b_t[i] + sqrt_dt*random.normal(0, dt)
		n_t[i+1] = n_t[0]*exp((a-0.5*b**2)*t[i+1] + b*b_t[i])
		n_t_list.append(n_t[i+1])
	return n_t_list

#euler solution
def eulersde(x_0, t_0, t_f, dt, f, g):
	t = linspace(t_0,t_f,1/dt)
	n = t.shape[0]
	sqrt_dt = sqrt(dt)
	x_t = zeros((n))
	x_t[0] = x_0
	x_t_list = []
	x_t_list.append(x_t[0])
	for i in range(int(1/dt)-1):
		rand_var = random.normal(0, dt)
		x_t[i+1] = x_t[i] + f*x_t[i]*dt + g*x_t[i]*rand_var*sqrt_dt
		x_t_list.append(x_t[i+1])
	return x_t_list

#huen solution
def huensde(x_0, t_0, t_f, dt, a, b):
	t = linspace(t_0, t_f, 1/dt)
	n = t.shape[0]
	sdt = sqrt(dt)
	x = zeros((n))
	x[0] = x_0
	x_list = []
	x_list.append(x_0)
	for i in range(1, int(1/dt)):
		x_n = x[i-1]
		w_t = random.normal(0, dt)*sdt
		x_tilde = x_n+(a*x_n)* dt + (b*x_n) * w_t
		x_t = x_n+(0.5)*((a*x_n)+(a*x_tilde)) * dt + (
				(0.5)*((b*x_n)+(b*x_tilde))) * w_t
		x[i] = x_t
		x_list.append(x[i])
	return x_list

def run():
	dts = [2**-3, 2**-4, 2**-5, 2**-6]
	n = 100
	expected_euler_error = []
	expected_huen_error = []
	for j in range(size(dts)):
		euler = []
		huen = []
		exact = []
		for i in range(n):
			#append the array returned by the euler algorithm
			euler.append(eulersde(1,0,1,dts[j],1.5,0.1))
			#append the array returned by the huen algorithm
			huen.append(huensde(1,0,1,dts[j],1.5,0.1))
			#append the array returned by the exact algorithm
			exact.append(exactsde(1,0,1,dts[j],1.5,0.1))

		#average the values returned from each iteration
		euler_mean = mean(euler, axis=0)
		huen_mean = mean(huen, axis=0)
		exact_mean = mean(exact, axis=0)
		
		#estimate the error-squared	
		euler_err = (euler_mean-exact_mean)**2
		huen_err = (huen_mean-exact_mean)**2
		
		#plot euler error over huen error for each value of delta t
		plotxyz(linspace(0,1,1/dts[j]), euler_err, huen_err, 'b','r', 'euler-huen dt=2^-'+str(j+3), 0)
		print 'plot saved to file'
		expected_euler_error.append(mean(euler_err))
		expected_huen_error.append(mean(huen_err))
	plotxyz(dts, expected_euler_error, expected_huen_error, 'b', 'r','avg_error_vs_dt', 0)
	print 'plot saved to file'
	print 'done'

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

def main():
	run()
 
if __name__=='__main__':
	main()
