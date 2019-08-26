#include <iostream>
#include <vector>

using namespace std;

int main_10951(void) {

	int a, b;

	vector<int> vec;

	while (true) {
		cin >> a;
		cin >> b;

		if (getchar() == EOF)
			break;

		vec.push_back(a + b);
	}

	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << endl;

	return 0;
}