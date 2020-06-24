// Created by Robert Mulligan 6/24/2020
//
// This problem doesn't make much sense
// But find specific sizes when sorted
// Tried using set, but that does not allow duplicates

#include <iostream> 
#include <vector> 
#include <algorithm> 

int main() {
	
	int A, B, C, D; 
	std::cin >> A >> B >> C >> D; 

	std::vector<int> inputs; 

	inputs.emplace_back(A); 
	inputs.emplace_back(B); 
	inputs.emplace_back(C); 
	inputs.emplace_back(D); 

	std::sort(inputs.begin(), inputs.end()); 
	
	int result = inputs[0] * inputs[2]; // smallest length by smallest width

	std::cout << result << std::endl; 


	return 0; 
}
