#include <iostream>

using namespace std;

int main_4344(void) {

	int caseNum;

	cin >> caseNum;

	double* upAvgRate = new double[caseNum];

	for (int i = 0; i < caseNum; i++) {
		int studentNum;
		cin >> studentNum;
		int* scores = new int[studentNum];
		int scoreSum=0;
		for(int j=0;j<studentNum;j++){
			int scoreInput;
			cin >> scoreInput;
			scoreSum += scoreInput;
			scores[j] = scoreInput;
		}
		double scoreAvg = double(scoreSum) / double(studentNum);
		int countUpAvgStudent = 0;
		for (int j = 0; j < studentNum; j++) {
			if (scoreAvg<double(scores[j])) {
				countUpAvgStudent++;
			}
		}
		upAvgRate[i] = double(countUpAvgStudent)/double(studentNum)*100.0;
	}

	cout << fixed;
	cout.precision(3);

	for (int i = 0; i < caseNum; i++) {
		cout << upAvgRate[i];
		cout << '%' << endl;
	}


	return 0;
}