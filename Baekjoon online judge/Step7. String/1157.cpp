#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main_1157(void) {

	vector<int> alphabet_count_num_vec(26, 0);

	string str_input;

	cin >> str_input;

	transform(str_input.begin(), str_input.end(), str_input.begin(), ::toupper);

	for (int i = 0; i<int(str_input.length()); i++) {
		alphabet_count_num_vec[int(str_input[i]) - int('A')]++;
	}

	vector<int>::iterator iter= max_element(alphabet_count_num_vec.begin(), alphabet_count_num_vec.end());

	int index = distance(alphabet_count_num_vec.begin(), iter);

	
	int max_count = 0;
	for (int i = 0; i < int(alphabet_count_num_vec.size()); i++) {
		if (alphabet_count_num_vec[i] == *iter) {
			max_count++;
		}
	}

	if (max_count > 1) {
		cout << '?';
	}
	else {
		cout << char(int('A') + index);
	}

	return 0;
}