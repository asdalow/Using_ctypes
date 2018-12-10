#include "sum.h"

double sum(int np_array_length, double* np_array) {
	double _sum = 0;
	for(int i=0; i<np_array_length; i++){
		_sum+=np_array[i];
	}	
	np_array[0]++;
	return _sum;
}
