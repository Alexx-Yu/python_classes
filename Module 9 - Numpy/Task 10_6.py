import numpy as np
def get_chess(a):
    c=np.zeros((a,a))
    c[0::2,1::2]=1
    c[1::2,::2]=1
    return c

    
    
print(get_chess(1))
# array([[0.]])
print(get_chess(4))
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])