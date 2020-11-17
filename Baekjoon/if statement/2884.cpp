#include <iostream>

using namespace std;

int main_2884(void) {

	int inputHour, inputMinute;

	cin >> inputHour;
	cin >> inputMinute;

	int resultHour, resultMinute;

	if (inputMinute - 45 < 0) {
		if (inputHour == 0) {
			resultHour = 23;
		}
		else {
			resultHour = inputHour - 1;
		}
		resultMinute = 60 - (45 - inputMinute);
	}
	else {
		resultMinute = inputMinute - 45;
		resultHour = inputHour;
	}

	cout << resultHour;
	cout << ' ';
	cout << resultMinute;

	return 0;
}