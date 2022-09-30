import numpy as np
def shuffle_seed(array):
    x=np.random.randint(0,2**32)
    np.random.seed(x)
    array_seed=np.random.permutation(array)

    return array_seed, x


array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# (array([1, 3, 2, 4, 5]), 2332342819)
print(shuffle_seed(array))
# (array([4, 5, 2, 3, 1]), 4155165971)