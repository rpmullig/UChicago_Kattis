// Created by Robert Mulligan
//
// Solid example of a datastructure usage
// The maps forms a tree with pairs and iterates in order

#include <iostream> 
#include <map>
#include <string>

int main() {
	
	int N; 
	std::cin >> N; 

	std::string input_one, input_two; 

	std::map<int, std::string> container; // typically implemented as a binary search tree  

	int diameter; 
	std::string color; 

	for(int i = 0; i < N; ++i){
				
		std::cin >> input_one >> input_two; 

		if(input_one[0] < 65) { // input -> diameter color
			
			diameter = std::stoi(input_one); 
			color = input_two; 
			

			container.insert(std::pair<int, std::string>(diameter, color)); 
		} else{ // input -> color radius 

			diameter = std::stoi(input_two) * 2; // get in terms of diameter
			color = input_one; 

			container.insert(std::pair<int, std::string>(diameter, color)); 
		}
	}
	// print out the c++ map
	for(auto it = container.cbegin(); it != container.cend(); ++it){

		std::cout << it->second << std::endl; 
	}

	return 0; 
}
