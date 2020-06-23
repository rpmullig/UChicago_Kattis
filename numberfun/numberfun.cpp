// Created by Robert Mulligan 6/23/2020
//
//
// This problem runs slow due to logic 0.02 second of CPU time
// but that speeds up writting it like this 
// Alternatively could have written as a switch case or if statements

#include <iostream> 

int main() {
	
	int N; 
	std::cin >> N; 

	int a, b, c; 
	bool valid; 

	for(int i = 0; i < N; ++i) {
		std::cin >> a >> b >> c; 

		valid = a + b == c ||
			a - b == c ||
			b - a == c ||
			(a / b == c && a % b == 0) || // no remainder 
			(b / a == c && b % a == 0) || 
			a * b == c; 

		if(valid) {
			std::cout << "Possible" << std::endl; 
		} else {
			std::cout << "Impossible" << std::endl; 
		}
	}

	return 0; 
}
