// Created by Robert Mulligan 6/20/2020
//

#include <iostream>

int main() {
	
	std::string input; 
	std::cin >> input; 
	
	int word_length = input.size() / 3; 

	for(int i = 0; i < word_length; ++i){
		
		if(input.at(i) == input.at(word_length + i)) {
			std::cout << input.at(i); // at least 2/3 majority 
		}
		else {
			std::cout << input.at(i + 2*word_length); // third word 
			}
	} 
	
	std::cout << "\n"; // new line after word is printed

	return 0; 
}
