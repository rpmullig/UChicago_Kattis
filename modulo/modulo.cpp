// Created by Robert Mulligan
//
//

#include <iostream> 
#include <set>

int main() {


	std::set<int> count; 
	int input; 

	while(std::cin >> input){

		count.insert(input % 42); 
	}

	std::cout << count.size() << std::endl; 

	return 0; 
}
