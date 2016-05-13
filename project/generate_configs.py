import random as rand
from numpy import *
from test_grid import test_grid as grid
from pad import pad

def generate_configs(l, h, j, initial_lattice, n_configs, n_usable_configs, t_tilde):
	lattice_full = zeros((l, l, n_configs))
	lattice = initial_lattice

	for x in range(0, n_configs):
		for t in range(0, l**2):
			r = floor(rand.random()*l)
			c = floor(rand.random()*l)
			new_lattice = lattice
			new_lattice[r, c] *= -1 #flip randomly selected lattice sites 
			padded_new_lattice = pad(new_lattice)
			[accepted, accepted_prob] = grid(h, j, padded_new_lattice, r, c, t_tilde)
			if accepted:
				lattice = new_lattice

		lattice_full[:, :, x] = lattice

	lattice_full = delete(lattice_full, range(0, n_configs - n_usable_configs), 2)
	return lattice_full
