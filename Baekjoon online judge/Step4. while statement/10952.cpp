#include <iostream>
#include <vector>

using namespace std;

int main_10952(void) {

	int a, b;

	vector<int> vec;

	while (true) {
		cin >> a;
		cin >> b;
		
		if (a == 0 && b == 0)
			break;

		vec.push_back(a + b);
	}

	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << endl;

	return 0;
}