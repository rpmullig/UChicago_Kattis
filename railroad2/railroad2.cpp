// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream>

int main() {

	int X, Y; 
	std::cin >> X >> Y; 

	if(Y % 2 == 0){ std::cout << "possible" << std::endl; }
	else { std::cout << "impossible" << std::endl; }

	return 0; 
}
