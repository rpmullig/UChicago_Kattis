// Created by Robert Mulligan 6/22/2020
//
// I should look at examples of how other people did this one
// It's much harder than it looks
//
// the problem statement is a bit confusing -- so I had to adjust


#include <iostream>
#include <vector>
#include <algorithm> // max_element 
#include <iterator> // distance
#include <map>

int main() {
	std::map<char,int> m;
	std::string input;

	while(std::cin >> input) {
		m[input[0]]++;
	}


	int best = 0;
	for(auto card : m) {
		best = std::max(best, card.second);
	}

	std::cout << best << std::endl;
}
