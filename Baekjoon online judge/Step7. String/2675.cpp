#include <iostream>
#include <string>
using namespace std;

int main_2675(void) {

	int case_num;
	int repeat_num_array[1000];
	string str_array[1000];

	cin >> case_num;

	for (int i = 0; i < case_num; i++) {
		cin >> repeat_num_array[i] >> str_array[i];
	}

	for (int i = 0; i < case_num; i++) {
		for (int j = 0; j < int(str_array[i].length()); j++) {
			for (int k = 0; k < repeat_num_array[i] ; k++)
				cout << str_array[i][j];
		}
		cout << endl;
	}


	return 0;
}