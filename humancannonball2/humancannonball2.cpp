// Created by Robert Mulligan 6/20/2020
//

#include <iostream>
#include <cmath> 

int main() {

	int N; 	
	std::cin >> N; 
	
	double v, theta, x, h_1, h_2; 
	const double g = 9.81;

	double t, y; 

	for(int i = 0; i < N; ++i){
		std::cin >> v >> theta >> x >> h_1 >> h_2; 
			
		theta = (theta * M_PI) / 180; // convert to radians for cmath library 

		t = x / (v * cos(theta));
		y = (v * t * sin(theta)) - (0.5f * g * pow(t,2)); 


		// std::cout << "h_1: " << h_1 << " h_2: " << h_2 << " y: " << y << std::endl; 

		if(y - h_1 >= 1.0f && h_2 - y >= 1.0f){
			std::cout << "Safe" << std::endl; 
		} else {
			std::cout << "Not Safe" << std::endl; 
		}
	}

	return 0; 
}
