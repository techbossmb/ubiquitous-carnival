import goodness_of_fit_lcg
import goodness_of_fit_rand
import goodness_of_fit_boxmuller
import goodness_of_fit_cauchy
import goodness_of_fit_gamma

def main():
	print 'Brewing numbers... '
	goodness_of_fit_lcg.main()#question 1
	print '\n'
	goodness_of_fit_rand.main()#question 2
	print '\n'
	goodness_of_fit_boxmuller.main()#question 3
	print '\n'
	goodness_of_fit_cauchy.main()#question 4
	print '\n'
	goodness_of_fit_gamma.main()#question 5
	print '\nDone.'

if __name__ =='__main__':
	main()
