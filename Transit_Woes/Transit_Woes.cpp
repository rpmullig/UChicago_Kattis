// Created by Robert Mulligan 6/19/2020
//

#include <iostream>

int main(){
	
	int s, t, n; 
	std::cin >> s >> t >> n; // take in the first line descriptor values
	
	int current_time = s; 
	int d[n+1], b[n], c[n]; 
	
	// read line #2 drop off walks -- note n+1
	for(int i = 0; i < n+1; ++i){
		std::cin >> d[i]; 
	}

	// read line #3 bus ride time
	for(int i = 0; i < n; ++i){
		std::cin >> b[i]; 
	}

	// read line #4 intervals of bus times 
	for(int i = 0; i < n; ++i){
		std::cin >> c[i]; 
	}

	current_time += d[0]; // walk to the first bus 

	for(int i = 0; i < n; ++i){
		if(current_time % c[i] != 0){
			current_time += c[i] - current_time % c[i]; // time remaining for bus to show
		} 
		current_time += b[i] + d[i+1]; // ride bus and walk to next stop 
	}	


	if(current_time > t) { 
		std::cout << "no" << std::endl; 
	}else{
		std::cout << "yes" << std::endl;
	}


	return 0; 
}
