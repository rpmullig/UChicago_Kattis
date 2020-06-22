// Created by Robert Mulligan
//
//

#include <iostream>

int main() {
	
	int G, S, C; 
	std::cin >> G >> S >> C; 

	int purchase_power = G * 3 + S * 2 + C * 1; 

	if(purchase_power <= 1) {std::cout << "Copper" << std::endl; return 0; }

	switch(purchase_power) {
		case 2:
			std::cout << "Estate or Copper" << std::endl; 
			break; 
		case 3:
			std::cout << "Estate or Silver" << std::endl; 
			break;
		case 4: 
			std::cout << "Estate or Silver" << std::endl;
			break; 
		case 5:
			std::cout << "Duchy or Silver" << std::endl; 
			break; 
		case 6: 
			std::cout << "Duchy or Gold" << std::endl; 
			break; 
		case 7: 
			std::cout << "Duchy or Gold" << std::endl;
			break; 
		default: 
			std::cout << "Province or Gold" << std::endl; 
			break; 
	}

	return 0; 
}
