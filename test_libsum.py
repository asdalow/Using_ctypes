import ctypes
import numpy as np

def ctypes_np_array_sum(np_array):
	libsum = ctypes.CDLL("./libsum.so.1") # loads the shared library
	libsum.sum.restype = ctypes.c_double # define mean function return type
	libsum.sum.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)] # define arguments types

	np_ar_c = np_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
	
	return libsum.sum(np_array.size, np_ar_c)
