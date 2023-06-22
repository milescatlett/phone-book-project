import multiprocessing as mp
import numpy as np
from time import time

print("Number of Cores: ", mp.cpu_count())

#prepare data
np.random.RandomState(100)
array = np.random.randint(0, 100, size=[20000, 5])
data = array.tolist()
print(data[:5])
