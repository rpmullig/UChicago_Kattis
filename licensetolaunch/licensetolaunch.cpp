// Created by Robert Mulligan
//
// I tried a couple different methods
// None could improve the speed of the code
// SO, it's very odd :/ 

#include <iostream>
#include <vector> 
#include <algorithm> 

int main(){

	int n; 
	std::cin >> n; 

	std::vector<int> inputs(n); 
	int input; 

	for(int i = 0; i < n; ++i){  
		std::cin >> input; 
		inputs[i] = input; 
	}

	int index = std::distance(inputs.begin(), std::min_element(inputs.begin(), inputs.end())); 


	std::cout << index << std::endl; // print index of the day 

	return 0; 
}
