from numpy import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats
from scipy.integrate import quad
import writer
from generate_configs import generate_configs
from pad import pad


def main():
    l = 15
    h = 0.1
    j = 1
    n_configs = 250
    n_usable_configs = 200
    temps = linspace(10,.5,20)
    energy = zeros((len(temps), 1))
    initial_energy = ones((l, l))
    last_lattice = initial_energy
    
    for iTemp, temp in enumerate(temps):
        lattice = generate_configs(l, h, j, last_lattice, n_configs, n_usable_configs, temp)
        lattice_pad = zeros((l+2, l+2, n_usable_configs))
        for config in range(n_usable_configs):
            lattice_pad[:,:,config] = pad(lattice[:,:,config])
        
        north = lattice_pad[0:-2, 1:-1, :]
        south = lattice_pad[2:, 1:-1, :]
        east = lattice_pad[1:-1, 2:, :]
        west = lattice_pad[1:-1, 0:-2, :]
        
        f = -1 * h * sum(lattice)
        s = -1 * 0.5*j * sum(lattice * 
            (north + south + east + west))
        energy_temp = (f+s)/float(n_usable_configs)
        energy[iTemp] = energy_temp
        #print('energy for ', temp, ' = ', energy_temp)
        last_lattice = lattice[:,:,-1]
    #print(energy)
    print size(temps)
    print size(energy)
    plotxy(temps, energy)
    
    
def plotxy(x,y):
	plt.figure('hw 1 figure')
	plt.xlabel('Temperature')
	plt.ylabel('Number of stable spins')
	plt.plot(x,y,'bo')
	plt.savefig('result/fig1')
	plt.show()

if __name__=='__main__':
    main()
