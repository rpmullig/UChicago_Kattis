// Created by Robert Mulligan 6/20/2020
//
// I had to research how to do this one. Very challenging 

#include <iostream>
#include <cmath>

int main() {

	int S; 
	std::cin >> S; 
	std::cout << S << ":" << std::endl; 

	int r; 

	for(int i = 2; i <= (S/2)+1; ++i) {
		r = S % (2 * i - 1); // at least one row of 2 
		if(r == 0 || r - i  == 0) {
			std::cout << i << "," << i-1 << std::endl; 
		}
		r = S % i; 
		if(r == 0) {
			std::cout << i << "," << i << std::endl; 
		}
	
	}
	std::cout << std::endl; // create a space for print output
	
	return 0; 
}
