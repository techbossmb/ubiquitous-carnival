from numpy import *
import writer as writer

#ross chapter 12 question 9
def main():
	r = zeros((1e6,3))
	for i in range(r.shape[0]):
		for j in range(r.shape[1]):
			r[i,j] = random.exponential()
	c1 = r[:,0] + 2*r[:,1] + 3*r[:,2]
	# ques a
	id_a = c1 > 15
	#ques b
	id_b= c1 < 1
	out_a = r[id_a, 0] + 2*r[id_a, 1] + 3*r[id_a, 2]
	out_b = r[id_b, 0] + 2*r[id_b, 1] + 3*r[id_b, 2]
	writer.write('')
	writer.append('a: '+str(mean(out_a)))
	writer.append('b: '+str(mean(out_b)))

if __name__=='__main__':
	main()
