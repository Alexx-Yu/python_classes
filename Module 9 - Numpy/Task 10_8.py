import numpy as np
def min_max_dist(*vectors):
    a=[]
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            a.append(np.linalg.norm(vectors[i]-vectors[j]))
    return min(a), max(a)
    


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)