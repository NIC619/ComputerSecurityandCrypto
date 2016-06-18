#include <iostream>
#include <unordered_map>
int main() {
	std::unordered_map<int, int> ht;
	for (int i = 0; i < 50000; i++) {
		int x;
		std::cin >> x;
		ht[x] = i;
	}
	return 0;
}
