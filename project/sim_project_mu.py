from numpy import *

def runProcess():
	L,k,gam,mu,colr = 10, 1, 4, 0.1, 1
	N = L**2
	mulist = mu
	rho = 1 + (k * exp((gam/2.0)*2 - mu))
	nu = 1
	tmax = 10
	h0 = zeros((L,L))
	h = h0
	lam = 1/float(N*rho)
	t = 0
	ntests = 10
	
	tlist = zeros(10**5)
	tind = 1
	
	while t <= 20:
		tlist[tind] = t
		tind = tind + 1
		tp = -1*log(random.uniform())/float(1/float(lam))
		t = t + tp
	tlist = tlist[1:tind-1]
	havgvsmu = zeros((tind-1, ntests, len(mulist)))
	havglist = zeros((tind-1, ntests))
	roughlist = zeros((tind-1, ntests))
	roughvsmu = zeros((tind-1, ntests, len(mulist)))
	monolayervsmu = zeros((tind-1, ntests, len(mulist)))
	mmodlist = zeros((tind-1, ntests))
	coverlist = zeros((tind-1, ntests))
	covervsmu = zeros((tind-1, ntests, len(mulist)))

	for muind in range(len(mulist)):
		mu = mulist(muind)
		for testind in range(len(ntests)):
			hgrid = growth120(tind, h0, gam, k, mu)
			hpad = zeros((L+2, L+2, tind-1))
			for ind in range(
#in progress - marker
def main():
	runProcess()	

if __name__=='__main__':
	main()
