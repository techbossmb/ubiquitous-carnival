import lcg
import shuffled_lcg
import py_random

def main():
	print 'Crunching numbers... '
	lcg.main()#question 1
	shuffled_lcg.main()#question 2
	py_random.main()#question 3
	print 'Done.\nGraphs and covariance matrices saved to "result" directory.'

if __name__ =='__main__':
	main()	
