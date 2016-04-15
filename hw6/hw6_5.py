from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import writer

def operation():
	l,H,J=15,0.1,1
	nbr_configs, nbr_configs2use = 250,200
	tt_list = [x/10.0 for x in range(100,0,-5)]

	expg_sigma = zeros([size(tt_list),1])
	
	m0 = random.random((l,l))*2 -1
	last_latt = m0

	for tt in range(tt_list):
		latt3D = generateConfigs(l, H, J, last_latt, nbr_configs, nbr_configs2use, tt_list[tt])	
		latt3D_pad = zeros(([l+2, l+2, nbr_configs2use))
		
		for cind in range(nbr_configs2use):
			latt3D_pad[:,:,cind] = mpad(latt3D[:,:,cind])
		
		north = latt3D_pad[0:-2, 1:-1, :]
		south = latt3D_pad[2:, 1:-1, :]
		east = latt3D_pad[1:-1, 2:, :]
		west = latt3D_pad[1:-1, 0:-2, :]

		stable_spins3D = (latt3D==north) and (latt3D==south) and (latt3D==east) and (latt3D==west)
		g_sigma = sum(stable_spins3D)
		expg_sigma[tt] = sum(g_sigma)/float(nbr_configs2use)
		last_latt = latt3D[:,:,-1]
	plotxy(tt_list, expg_sigma,'Figure 5')	

def plotxy(x,y,title):
	plt.figure(title)
	plt.xlabel('Temperature')
	plt.ylabel('Number of stable spins')
	plt.plot(x,y,'bo')
	plt.savefig('result/'+title)
	plt.show()

def main():
	print("hello")
	operation()

if __name__=="__main__":
	main()
