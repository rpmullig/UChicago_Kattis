// Created by Robert Mulligan 6/19/2020
//

#include <iostream> 
#include <set>

int main() {

	std::set<std::string> previous_words; 

	std::string input; 
	while(std::cin >> input){
		if(previous_words.find(input) != previous_words.end()){
			std::cout << "no" << std::endl;
			return 0; 
		} else{
			previous_words.insert(input); 
		}		

	}

	std::cout << "yes" << std::endl; 


	return 0; 

}
