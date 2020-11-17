#include <iostream>

using namespace std;

int main_10872(void) {

	int n;
	
	cin >> n;

	int result = 1;

	for (int i = n; i > 0; i--) {
		result *= i;
	}

	cout << result << endl;

	return 0;
}