#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b) {
	return a > b;
}

int main_1546(void) {

	int n;
	cin >> n;

	vector<int> vec;
	

	int inputTmp;
	for (int i = 0; i < n; i++) {

		cin >> inputTmp;
		vec.push_back(inputTmp);
	}

	sort(vec.begin(), vec.end(), compare);

	int maxScore = vec[0];
	double sum = 0.0;

	for (int i = 0; i < int(vec.size()); i++) {
		sum+=(double(vec[i]) / double(maxScore) * 100.0);
	}

	cout << sum / n << endl;

	
	return 0;
}