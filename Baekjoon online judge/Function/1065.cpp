#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool HanCheck(int n);

int main_1065(void) {

	int n;
	cin >> n;

	int hanCount = 0;

	
	for (int i = 1; i <= n; i++) {
		if (HanCheck(i) == true)
			hanCount++;
	}

	cout << hanCount << endl;

	return 0;
}

bool HanCheck(int n) {
	string nString = to_string(n);
	vector<int> vec;

	for (int i = 0; i < int(nString.length()); i++) {
		vec.push_back(int(nString[i]) - 48);
	}
	bool hanCheck = true;
	if (n > 10) {
		int d = vec[1] - vec[0];
		for (int i = 2; i < int(vec.size()); i++) {

			if (vec[i] - vec[i - 1] != d) {
				hanCheck = false;
				break;
			}

		}
	}
	return hanCheck;
}