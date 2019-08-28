#include <iostream>
#include <string>
#include <set>

using namespace std;

void EraseNotSelfNum(int num, set<int>& s);

int main_4673(void){

	set<int> s;
	set<int>::iterator iter;
	for (int i = 1; i <= 10000; i++)
		s.insert(i);

	for (iter = s.begin(); iter != s.end(); iter++) {
		EraseNotSelfNum(*iter, s);
	}

	for (iter = s.begin(); iter != s.end(); iter++) {
		cout << *iter << endl;
	}

	return 0;
}

void EraseNotSelfNum(int num, set<int> &s) {

	string stringOfNum = to_string(num);

	int nextNum = num;

	for (int i = 0; i < int(stringOfNum.length()); i++) {
		nextNum += int(stringOfNum[i]) - '0';
	}

	if (s.find(nextNum) != s.end()) {
		s.erase(nextNum);
		return EraseNotSelfNum(nextNum, s);
	}
	else {
		return;
	}
}