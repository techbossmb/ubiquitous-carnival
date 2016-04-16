from numpy import *

def pad(m):
   #print m.shape
   rowLen = m.shape[0]
   m_tmp = ones((rowLen,1))
   tmp_m = m[:,-1]
   for i in range(rowLen):
      m_tmp[i] = tmp_m[i]
   m_tmp0 = ones((rowLen,1))
   tmp_m0 = m[:,0]
   for j in range(rowLen):
      m_tmp0[j] = tmp_m0[j]
   #print m_tmp.shape
   #print tmp_m.shape
   #m[:,1] should be a coulmn matrix that can be concatenated
   m1 = concatenate((m_tmp, m, m_tmp0), axis=1)
   #print m1
   m_tmp1 = ones((1,rowLen))
   #print m_tmp1.shape
   tmp_m1 = m[-1,:]
   #print m_tmp1.shape
   iters = size(tmp_m1)
   for k in range(iters):
      m_tmp1[0,k] = tmp_m1[k]
   #print m_tmp1.shape
   a = zeros((1,1))
   #print a.shape
   mgrid1 = concatenate((a, m_tmp1, a), axis=1)
   #print mgrid1
   m_tmp2 = ones((1,rowLen))
   tmp_m2 = m[0,:]
   iters = size(tmp_m2)
   for l in range(iters):
      m_tmp2[0,l] = tmp_m2[l]
   mgrid2 = concatenate((a, m_tmp2, a), axis=1)
   mgrid = concatenate((mgrid1, m1, mgrid2), axis=0)
   return mgrid
   #temp =numpy.array([[m[:, m.shape[0]-1]], m, m[:,0]])
   #pad = numpy.array([[0, m[m.shape[0]-1, :], 0], 
            #[temp], 
            #[0, m[0, :], 0]])
   # return pad
