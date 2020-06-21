// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream>
#include <cmath> 

int main(){
	
	int T; 
	std::cin >> T; 

	int curr, prev, bound;  

	for(int row = 0; row < T; ++row){
		
		// read in first elements in the row
		std::cin >> prev; 
		std::cin >> curr;
		bound = 0; 

		while(curr != 0){
			
			bound += std::max(0, curr - 2 * prev); 

			prev = curr; 
			std::cin >> curr; 	

		}
		std::cout << bound << std::endl; 
		
	}

	return 0; 
}
