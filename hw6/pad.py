from numpy import *

def pad(m):
   print m[:,-1].shape
  #m[:,1] should be a coulmn matrix that can be concatenated
   m1 = concatenate((transpose(m[:,-1]), m,transpose(m[:,0])), axis=1)
   print m1
   mgrid1 = concatenate((0, m[-1,:], 0), axis=1) 
   mgrid2 = concatenate((0, m[0,:], 0), axis=1)
   mgrid = concatenate((mgrid1,m1,mgrid2), axis=0)
   return mgrid
   #temp =numpy.array([[m[:, m.shape[0]-1]], m, m[:,0]])
   #pad = numpy.array([[0, m[m.shape[0]-1, :], 0], 
            #[temp], 
            #[0, m[0, :], 0]])
   # return pad
