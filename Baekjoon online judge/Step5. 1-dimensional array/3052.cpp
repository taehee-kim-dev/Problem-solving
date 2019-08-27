#include <iostream>
#include <vector>

using namespace std;

int main_3052(void) {

	vector<int> vec(42, 0);


	int tmp;
	for (int i = 0; i < 10; i++) {
		cin >> tmp;
		vec[tmp % 42]++;
	}

	int count = 0;
	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] > 0)
			count++;
	}

	cout << count;

	return 0;
}