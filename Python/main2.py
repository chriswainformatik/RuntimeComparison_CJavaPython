import random
import time
import numpy as np

n = 500

#populate the matrices with random values between 0.0 and 1.0
A = [[random.random() for row in range(n)] for col in range(n)]
B = [[random.random() for row in range(n)] for col in range(n)]

start = time.time()
#matrix multiplication
C = np.matmul(A,B)

end = time.time()
print("Elapsed time in seconds %0.6f" % (end-start))