// Created by Robert Mulligan 6/20/2020
//

#include <iostream> 


int main(){
	
	bool found_fbi = false; 
	std::string input{}; 
	for(int i = 0; i < 5; ++i){
		std::cin >> input; 
		for(int j = 0; j < input.size()-2; ++j){
			if(input.at(j) == 'F' && input.at(j+1) == 'B' && input.at(j+2) == 'I'){
				std::cout << (i+1) << ' '; 
				found_fbi = true; 
				j = input.size(); // break out of the j loop	
			}
		}	
	
	}

	if(!found_fbi){
		std::cout << "HE GOT AWAY!" << std::endl; 
	}else{
		std::cout << "\n"; // new line for reading purposes when just numbers
	}

	return 0; 
}
