#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

int main_2577(void) {

	vector<int> vec(10, 0);
	
	int mul=1, tmp;

	for (int i = 0; i < 3; i++) {
		cin >> tmp;
		mul *= tmp;
	}

	string numStr = to_string(mul);
	int strLen = (int)(numStr.length());
	int index;

	for (int i = 0; i < strLen; i++) {
		index = (int)numStr[i] - 48;
		vec[index]++;
	}

	
	for (int i = 0; i < 10; i++) {
		cout << vec[i] << endl;
	}

	return 0;
}