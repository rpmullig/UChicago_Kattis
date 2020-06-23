// Created by Robert Mulligan
//
//

#include <iostream> 

int main() {

	std::string input; 
	std::cin >> input; 

	double whitespace_count{}, lower_count{}, upper_count{}, symbols_count{}; 
	for(char l : input){

		if(l == '_') {
			++whitespace_count; 
		} else if (l >= 65 && l <= 90) {
			++upper_count; 
		} else if (l >= 97 && l <= 122){
			++lower_count; 
		} else{
			++symbols_count; 
		}
	}

	std::cout << (double) (whitespace_count / input.size()) << std::endl; 	
	std::cout << (double) (lower_count / input.size()) << std::endl; 
	std::cout << (double) (upper_count / input.size()) << std::endl; 
	std::cout << (double) (symbols_count / input.size()) << std::endl; 
	
	return 0; 
}
