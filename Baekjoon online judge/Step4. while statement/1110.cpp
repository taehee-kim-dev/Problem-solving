#include <iostream>

using namespace std;

int main_1110(void) {

	int n;
	cin >> n;

	int a, b, c, startNumber, newNumber, count = 0;

	startNumber = n;

	while (true) {
		
		a = startNumber / 10;
		b = startNumber % 10;
		c = a + b;

		newNumber = b * 10 + c % 10;
		count++;

		if (n == newNumber)
			break;
		
		startNumber = newNumber;
	}

	cout << count;

	return 0;
}