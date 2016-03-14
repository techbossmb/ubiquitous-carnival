import monte_carlo as montecarlo
import randomwalk as walker
import writer as writer

def main():
	print("Starting...")
	writer.write("")
	montecarlo.main()
	walker.main()
	print("Done.\nResults saved in result/result.txt")

if __name__=="__main__":
	main()
