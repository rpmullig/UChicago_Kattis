// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream> 
#include <string> 

int main() {

	int N; 
	std::cin >> N;  

       	std::string cond = "Simon says "; // condition 
	int cond_l = cond.size(); 

	
	std::string input; 	

	// this is used to clean the first line. 
	// a better alternative is needed
	// Understanding why the line std::cin >> N
	// does not advance to the next line in the input
	// is important 
	std::getline(std::cin, input); 

	for(int i = 0; i < N; ++i){

		// http://www.cplusplus.com/reference/string/string/find/

		std::getline(std::cin, input); 

		if(input.substr(0, cond_l).find(cond) != std::string::npos){

			std::cout << input.substr(cond.size()) << std::endl; 
		}
	}

	return 0; 
}
