// Created by Robert Mulligan 6/20/2020
//
//

#include <iostream> 
#include <cmath>

int main(){

	int P; 
	std::cin >> P; 

	unsigned int n; 
	int K, b;
       	int ssd; 	
	int num_length; 
	int tmp_a; 

	for(int i = 0; i < P; ++i){
		std::cin >> K >> b >> n; 
		ssd = 0; 

		while(n > 0) {
			ssd += pow( n%b, 2); 
			n /= b; 
		}

		std::cout << K << " " << ssd << std::endl; 
	}

	return 0; 
}
