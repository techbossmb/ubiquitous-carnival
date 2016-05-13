import random as rand
from numpy import *
#from hw6
def test_grid(h, j, lattice, r, c, temp_tilde):
	sigma = lattice[r, c]
	d_u = -((2 * h * sigma) + (2 * j * sigma * (lattice[r+1, c] + lattice[r-1, c] + lattice[r, c+1] + lattice[r, c-1])))
	q = exp(-d_u / float(temp_tilde))
	pr = min(1, q)
	result = (rand.random() <= pr)
	return [result, pr]
