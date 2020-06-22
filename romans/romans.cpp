// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream>
#include <cmath>

int main() {

	double X; 
	std::cin >> X; 

	double roman_to_mile = 5280.0f / 4854.0f ; 

	std::cout << (int) std::round(X * 1000.0f * roman_to_mile) << std::endl; 

	return 0; 
}
