#include <iostream>

using namespace std;

int main_2588(void) {

	int firstInput, secondInput;
	cin >> firstInput;
	cin >> secondInput;
	
	int eachDigitArray[3], tmp;
	eachDigitArray[2] = secondInput / 100;
	tmp = secondInput % 100;
	eachDigitArray[1] = tmp / 10;
	tmp = secondInput % 100 % 10;
	eachDigitArray[0] = tmp;

	int sum = 0, powNum = 1;
	for (int i = 0; i < 3; i++) {
		tmp = firstInput * eachDigitArray[i];
		cout << tmp << endl;
		sum += tmp * powNum;
		powNum *= 10;
	}

	cout << sum << endl;

	return 0;
}