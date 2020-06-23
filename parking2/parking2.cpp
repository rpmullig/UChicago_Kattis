// Created by Robert Mulligan
//
// This was a good problem
// issues with using a map and iterating backward
// learning to utilize vectors more, especially with sort
// utilized a lambda on sorting
// emplace_back did not work, alternated at vs overloaded operator '[]'
// for accessing vectors
//

#include <iostream> 
#include <vector> // tried to use a set, but iteration was annoying 
#include <algorithm> 

int main() {

	int t;  
	std::cin >> t;

	int n, dist, val; 

	for(int i = 0; i < t; ++i) {

		dist = 0; 

		std::cin >> n;		
		std::vector<int> values(n); 
		
		for(int j = 0; j < n; ++j) {
			std::cin >> val;  
			values[j] = val; // emplace_back did not work here -- curious as to why
		}
		
		// lambda function for sorting 
		std::sort(values.begin(), values.end(), [](auto a, auto b) { return a < b; }); // non-decreasing order

		// note the plus 1 to start ate the second item.
		//std::cout << "Values: "; 
		for(int j = 1; j < n; ++j){
			//std::cout << values.at(j); 
			dist += values.at(j) - values.at(j-1);  
		}
		//std::cout << std::endl << std::endl; 

		dist += values.at(n-1) - values.at(0); 

		std::cout << dist << std::endl; 
	}


	return 0; 
}
