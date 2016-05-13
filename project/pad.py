from numpy import *

def pad(lattice):
	first_col = array([lattice[:, 0]]).T
	last_col = array([lattice[:, -1]]).T
	temp = hstack((last_col, lattice, first_col)) # row matrix

	first_row = insert(lattice[-1, :], 0, 0)
	first_row = append(first_row, 0)
	last_row = insert(lattice[0, :], 0, 0)
	last_row = append(last_row, 0)
	pad = vstack((first_row, temp, last_row)) # column matrix

	return pad
