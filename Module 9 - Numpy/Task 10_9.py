import numpy as np
def any_normal(*vectors):
    a=[]
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            a.append(np.dot(vectors[i],vectors[j]))
    if min(a) == 0: return True
    else: return False




vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True