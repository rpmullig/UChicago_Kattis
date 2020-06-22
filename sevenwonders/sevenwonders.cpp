// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream>
#include <cmath> 

int main() {

	std::string input; 
	std::cin >> input; 

	double count_T{}, count_C{}, count_G{}; 

	for(char l : input){
		switch(l){
			case 'T':
				++count_T;
				break; 
			case 'C':
				++count_C; 
				break; 
			case 'G':
				++count_G; 
				break; 
		}
	}

	double result = std::pow(count_T, 2) + std::pow(count_C, 2) + std::pow(count_G, 2) + 7 * std::min(std::min(count_T, count_C), count_G); 

	std::cout << result << std::endl; 

	return 0; 
}
