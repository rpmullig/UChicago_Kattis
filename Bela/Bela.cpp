//
// Created by Robert Mulligan 6/19/2020
//

#include <iostream>

int main() {

	int solution = 0; 

	int N;
	char B; 	
	std::cin >> N >> B; 

	std::string input; 
	char suit; 
	int number; 
	for(int i = 0; i < 4*N; ++i){
		std::cin >> input; 
		suit = input[1]; 
		number = input[0]; 

		if(suit == B){

			switch(number){
				case 'A':
					solution += 11; 
					break;
				case 'K': 
					solution += 4; 
					break; 
				case 'Q': 
					solution += 3; 
					break; 
				case 'J':
					solution += 20; 
					break; 
				case 'T':
					solution += 10; 
					break; 
				case '9': 
					solution += 14; 
					break; 
				case '8': 
					break; 
				case '7': 
					break; 
			}
		}else {

			switch(number){

				case 'A': 
					solution += 11; 
					break; 
				case 'K': 
					solution += 4; 
					break; 
				case 'Q': 
					solution += 3; 
					break; 
				case 'J': 
					solution += 2; 
					break; 
				case 'T':
					solution += 10; 
					break; 
				case '9': 
					break; 
				case '8': 
					break; 
				case '7':
					break; 
			}
				
		}	
	}
	std::cout << solution << std::endl; // print solution
	return 0; 
}







