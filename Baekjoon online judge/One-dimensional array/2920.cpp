#include <iostream>
#include <vector>

using namespace std;

int main_2920(void) {

	vector<int> num_vec;

	int numInput;
	for (int i = 0; i < 8; i++) {
		cin >> numInput;
		num_vec.push_back(numInput);
	}

	bool descending = true, ascending = true;
	int tmp = num_vec[0];

	for (int i = 1; i < 8; i++) {
		if (tmp < num_vec[i])
			descending = false;
		if (tmp > num_vec[i])
			ascending = false;

		tmp = num_vec[i];
	}

	if (descending == true)
		cout << "descending";
	else if (ascending == true)
		cout << "ascending";
	else
		cout << "mixed";


	return 0;
}