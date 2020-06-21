// Created by Robert Mulligan
//
//
//

#include <iostream>

int main() {

    int n; 
    n = 0; 
    
    int speed, t_1, t_2, miles; 

    std::cin >> n; 

    while(n != -1) {
        
        // reset stack variables
        t_1 = 0;
        miles = 0; 

        for(int i = 0; i < n; ++i){
    
            std::cin >> speed >> t_2; 

            miles += speed * (t_2 - t_1); 

            t_1 = t_2; // set the new time for updates
            
        }

        std::cout << miles << " miles" << std::endl; 
        std::cin >> n; 
    }

    return 0; 
}
