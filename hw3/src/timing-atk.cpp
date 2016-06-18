#include <iostream>
#include <string>

#include "password.h" // std::string password = ...

bool compare(const std::string &s){
	if ( s.size() != password.size() ) return false;
	int n = s.size();
	for ( int i = 0; i < n; i++ ) {
		if ( s[i] != password[i] ) return false;
	}
	return true;
}

int main(){
	std::string input;
	std::cin >> input;
	if ( compare(input) ){
		std::cout << "This is the correct password!\n";
	}
}
