// Created by Robert Mulligan
//
//

#include <iostream>

int main() {

	int N; 
	std::cin >> N; 

	std::string input; 

	// needed to move the first line to the second 
	std::getline(std::cin, input);  

	for(int i = 0; i < N; ++i){
		std::getline(std::cin, input); 
		std::cout << input.size() << std::endl; 
	}

	return 0; 
}
