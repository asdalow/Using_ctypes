# Basic tutorial on how to use ctypes

Run: sh make.

It will create the library: libsum.so.1.

This library contains a sum function, you can see its definition in sum.h, sum.c. It receives a pointer to a double array, sums its contents, increases one of its elements and returns the previously calculated sum.

The file test_libsum.py wraps this C function with ctypes, so that we can give this function a numpy array and see it in action.

import_test.py imports the wrapper, creates a numpy array, and gives it to the wrapped C function. It prints the sum of the array, and to see that it really was working on the Python defined numpy array's elements, we call the function again. Now the sum value is increased by one, as was expected.

That's all!
