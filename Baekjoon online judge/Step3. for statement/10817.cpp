#include <iostream>

using namespace std;

int main_10817(void) {

	int a, b, c;

	cin >> a;
	cin >> b;
	cin >> c;

	int tmp;

	if (a > b) {
		tmp = a;
		a = b;
		b = tmp;
	}

	if (b > c) {
		tmp = b;
		b = c;
		c = tmp;
	}

	if (a > b) {
		tmp = a;
		a = b;
		b = tmp;
	}

	cout << b;

	return 0;
}