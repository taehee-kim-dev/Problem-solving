#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main_8958(void) {

	int n;
	cin >> n;

	vector<string> problemResultVector;
	vector<int> scoreVector;

	string tmpStringInput;

	for (int i = 0; i < n; i++) {
		cin >> tmpStringInput;
		problemResultVector.push_back(tmpStringInput);
	}

	for (int i = 0; i < n; i++) {
		int SumScore = 0;
		int ScoreCount = 0;
		int tmpScoreSum = 0;
		for (int j = 0; j<int(problemResultVector[i].length()); j++) {
			if (problemResultVector[i][j] == 'O') {
				ScoreCount++;
				tmpScoreSum += ScoreCount;
			}else {
				SumScore += tmpScoreSum;
				tmpScoreSum = 0;
				ScoreCount = 0;
			}
		}
		SumScore += tmpScoreSum;
		scoreVector.push_back(SumScore);
	}

	for (int i = 0; i < n; i++) {
		cout << scoreVector[i] << endl;
	}

	return 0;
}