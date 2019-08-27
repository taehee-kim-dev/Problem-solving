#include <iostream>

using namespace std;

int main_10818(void) {

	int n, min, max;

	cin >> n;

	int* arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	min = arr[0];
	max = arr[0];

	for (int i = 1; i < n; i++) {
		if (arr[i] < min)
			min = arr[i];

		if (arr[i] > max)
			max = arr[i];
	} 

	cout << min;
	cout << ' ';
	cout << max;

	delete[]arr;

	return 0;
}