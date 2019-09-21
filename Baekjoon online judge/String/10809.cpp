#include <iostream>
#include <string>

using namespace std;

int main_10809(void) {

	int result[26];

	for (int i = 0; i < 26; i++)
		result[i]=-1;

	string input_str;

	cin >> input_str;

	for (int i = 0; i < int(input_str.length()); i++) {
		if (result[(int)(input_str[i]) - (int)('a')] == -1) {
			result[(int)(input_str[i]) - (int)('a')] = i;
		}
	}

	for (int i = 0; i < 26; i++)
		cout << result[i] << ' ';

	return 0;
}