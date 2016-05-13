from numpy import *
import matplotlib.pyplot as plt
import pylab
from random import random
from growth_model import growth_model
from pad import pad

def main():
	gamma_test()
	#mu_test()


def gamma_test():
	gamma_list = [4]#, 3, 4]
	avg_traces = []
	mono_traces = []
	rough_traces = []
	coverage_traces = []

	for gamma in gamma_list:
		print("gamma: ", gamma)
		evaluate(gamma, 0.5)
		#[avg_plot, mono_plot, rough_plot, coverage_plot] = evaluate(gamma, .5)
		#avg_traces.append(avg_plot)
		#mono_traces.append(mono_plot)
		#rough_traces.append(rough_plot)
		#coverage_traces.append(coverage_plot)
	#plot(avg_traces, mono_traces, rough_traces, coverage_traces)

def mu_test():
	mu_list = {.1}#, .3, .5}
	avg_traces = []
	mono_traces = []
	rough_traces = []
	coverage_traces = []
	for mu in mu_list:
		print("mu:, ", mu)
		evaluate(4, mu)
		#[avg_plot, mono_plot, rough_plot, coverage_plot] = evaluate(4, mu)
		#avg_traces.append(avg_plot)
		#mono_traces.append(mono_plot)
		#rough_traces.append(rough_plot)
		#coverage_traces.append(coverage_plot)
	#plot(avg_traces, mono_traces, rough_traces, coverage_traces)


def evaluate(gamma, mu):
	l = 10
	k = 1
	n = l ** 2
	nu = 1
	h0 = zeros((l, l))
	rho = 1 + (k * exp((gamma / 2.0)*2-mu))

	beta = 1 / float(n*rho)
	num_tests = 10

	t = 0
	idx = 1

	times = zeros((10**5, 1))
	while t <= 20:
		times[idx] = t
		idx += 1
		time = -log(random()) / float(1 / float(beta))
		t += time
	times = times[:idx]
	times = squeeze(times)

	avg_list = zeros((idx, num_tests))
	rough_list = zeros((idx, num_tests))
	mono_layer_list = zeros((idx, num_tests))
	coverage_list = zeros((idx, num_tests))

	for iTest in range(num_tests):
		grid = growth_model(idx, h0, gamma, k, mu)
		h_pad = zeros((l+2, l+2, idx))

		for i in range(idx-1):
			h_pad[:, :, i] = pad(grid[:, :, i])

		end_x = h_pad.shape[0] - 1
		end_y = h_pad.shape[1] - 1
		north = h_pad[0:end_x - 1, 1:end_y, :]
		south = h_pad[2:end_x + 1, 1:end_y, :]
		east = h_pad[1:end_x, 2:end_y + 1, :]
		west = h_pad[1:end_x, 0:end_y - 1, :]
		r = sum(abs(grid-north) + abs(grid-south) + abs(grid-east) + abs(grid-west), 0)
		rough = sum(r,0) / float(2*(l**2))
		rough_list[:, iTest] = squeeze(squeeze(rough))

		grid[grid < 0] = 0
		avg_list[:, iTest] = squeeze(mean(mean(grid, 0), 0))
		mono_layer_list[:, iTest] = squeeze(floor((sum(sum(grid, 0), 0) / float(l ** 2))))
		coverage_list[:, iTest] = squeeze(sum(sum(grid >= nu, 0), 0 / float(l**2)))
	
	title = "figure" #"gamma-"+ str(gamma) + "mu-" + str(mu)
	plotxy(times, mean(mono_layer_list, 1), title)
	#avg_plot = Scatter(x=times, y=mean(avg_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
	#mono_plot = Scatter(x=times, y=np.mean(mono_layer_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
	#rough_plot = Scatter(x=times, y=np.mean(rough_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
	#coverage_plot = Scatter(x=times, y=np.mean(coverage_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
	#return [avg_plot, mono_plot, rough_plot, coverage_plot]
	
def plotxy(x, y, title):
	plt.figure(title)
	plt.xlabel('x')
	plt.ylabel('y')
	fig = plt.plot(x,y, 'bo')
	plt.savefig('result/'+title)
	plt.show()
'''
def plot(avg_traces, mono_layer_traces, rough_traces, coverage_traces):
    # plot stuff
    plot_avg(avg_traces)
    plot_mono(mono_layer_traces)
    plot_rough(rough_traces)
    plot_coverage(coverage_traces)


def plot_avg(avg_traces):
    plotly.offline.plot({
        "data": avg_traces,
        "layout": Layout(title="Average Layer Height vs Time")
    }, filename="layer.html")


def plot_mono(mono_layer_traces):
    plotly.offline.plot({
        "data": mono_layer_traces,
        "layout": Layout(title="Number of Mono-Layers vs Time")
    }, filename="layer.html")


def plot_rough(rough_traces):
    plotly.offline.plot({
        "data": rough_traces,
        "layout": Layout(title="Surface Roughness vs Time")
    }, filename="layer.html")


def plot_coverage(coverage_traces):
    plotly.offline.plot({
        "data": coverage_traces,
        "layout": Layout(title="Step Coverage vs Time")
    }, filename="layer.html")
'''

if __name__ == '__main__':
    main()
