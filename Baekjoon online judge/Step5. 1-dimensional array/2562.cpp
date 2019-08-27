#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main_2562(void) {

	vector<int> v;
	vector<int>::iterator iter;
	int val;

	for (int i = 0; i < 9; i++) {
		cin >> val;
		v.push_back(val);
	}

	iter = max_element(v.begin(), v.end());
	cout << *iter << endl;
	cout << iter - v.begin()+1;

	return 0;
}