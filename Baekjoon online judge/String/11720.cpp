#include <iostream>
#include <string>

using namespace std;

int main_11720(void) {

	int n;

	cin >> n;

	string nums;

	cin >> nums;

	int sum=0;
	for (int i = 0; i < n; i++) {
		sum += nums[i] - 48;
	}

	cout << sum;

	return 0;
}