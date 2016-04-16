import random
from numpy import *
from test_grid import test_grid
from pad import pad

def generate_configs(l, h, j, initial_lattice, 
        n_configs, n_usable_configs, t_tilde):
    
    lattice_full = zeros((l, l, n_configs))

    for x in range(n_configs):
        for t in range(l**2):
            r = random.random() * l
            c = random.random() * l
            new_lattice = initial_lattice
            new_lattice[r, c] = new_lattice[r,c] * -1
	    #print new_lattice.shape
            padded_new_lattice = pad(new_lattice)
            [accepted, accepted_prob] = test_grid(h, j, padded_new_lattice, r, c, t_tilde)
            if accepted:
                lattice = new_lattice
        lattice_full[:,:,x] = lattice
    size_z = lattice_full.shape[2]
    lattice3D = lattice_full[:,:,size_z-n_usable_configs:size_z]
    return lattice3D
