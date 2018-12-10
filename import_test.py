import test_libsum as tls
import numpy as np

arr = np.array([4,5,6, 1,2])
arr = arr.astype(np.float64) # must do it here, not in the wrapper!
print(tls.ctypes_np_array_sum(arr))
print(tls.ctypes_np_array_sum(arr))
