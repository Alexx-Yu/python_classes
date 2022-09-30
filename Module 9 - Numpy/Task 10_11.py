import numpy as np

def get_unique_loto(num):
    arr=np.zeros((num,5,5), dtype=np.int32)
    nums=np.arange(1,101)
    for i in range(num):
        arr[i]=np.random.choice(nums, (5,5), replace=False)
    return arr



print(get_unique_loto(3))
#array([[[26, 91, 73,  7, 16],
#       [46, 85, 78, 77, 51],
#       [84, 86, 55, 71, 58],
#       [17, 61, 50, 30, 97],
#       [66, 29, 38, 41, 32]],
# 
#      [[49, 32,  3, 21, 85],
#       [45,  8, 94, 46, 96],
#       [41, 38, 58, 37, 98],
#       [66, 77, 54, 80, 26],
#       [62, 63, 72,  5, 43]],
# 
#      [[55, 60,  6, 80, 97],
#       [23, 69, 94,  9, 24],
#       [17, 98, 27, 63, 79],
#       [84, 74, 51, 39, 54],
#       [77, 30, 48, 75, 85]]])