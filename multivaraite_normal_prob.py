# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:36:28 2019

@author: premp
"""

import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy.linalg import det
import math

x = np.array([[1,2,7],[9,6,1],[5,3,1]])
#y = np.array([[1],[2],[5]])
test = x = np.array([[1,2,7],[9,6,1],[5,3,1], [1,2,3]])


#np.dot(x, y)
#np.dot(x.T, y)

mu = np.mean(x, axis = 0)
print(mu)
sigma = np.cov(x)
pi = math.pi
#np.corrcoef(x)

x1 = np.array([1, 5,3])
#inv(sigma)

#np.exp(2*5*0)

#data = np.array(['a','b','c','d'])
#x = [100,101,102,103]
#s = pd.Series(data,index=x)
#print(s)

p = float(np.shape(x)[0])    #size of data matrix
m_d = np.dot(np.dot(x1-mu, inv(sigma)), x1-mu)  #mahalanobis distance
print(m_d)
mod_sigma = det(sigma)
print(mod_sigma)
pi = math.pi


#p_x = 1/((2*pi)^(p/2)*det(sigma)^0.5)*(np.exp(-1/2(np.dot(np.dot(x-mu, inv(sigma)), x-mu))))
p_x = 1/((2*pi)**(p/2)*mod_sigma**0.5)*(np.exp(-0.5*m_d))

print(p_x)