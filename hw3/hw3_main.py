import goodness_of_fit_lcg
import goodness_of_fit_rand
import goodness_of_fit_boxmuller
import goodness_of_fit_cauchy
import goodness_of_fit_gamma
import writer

def main():
	print 'Brewing numbers... '
	writer.write('GOODNESS OF FIT TEST FOR FIVE DISTRIBUTIONS\n')
	goodness_of_fit_lcg.main()#question 1
	writer.append('\n')
	goodness_of_fit_rand.main()#question 2
	writer.append('\n')
	goodness_of_fit_boxmuller.main()#question 3
	writer.append('\n')
	goodness_of_fit_cauchy.main()#question 4
	writer.append('\n')
	goodness_of_fit_gamma.main()#question 5
	print 'Done. Results written to result/result.txt'

if __name__ =='__main__':
	main()
