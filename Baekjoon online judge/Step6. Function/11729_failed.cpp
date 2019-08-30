#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

void hanoi(int from, int to, int tmp, int num, vector<pair<int, int>> &pv) {
	if (num == 1) {
		pv.push_back(make_pair(from, to));
		return;
	}
	else {
		hanoi(from, tmp, to, num - 1, pv);
		pv.push_back(make_pair(from, to));
		hanoi(tmp, to, from, num - 1, pv);
	}
}

int main(void) {

	int n;
	vector<pair<int, int>> pv;
	scanf_s("%d", &n);

	hanoi(1, 3, 2, n, pv);
	printf("%d\n", pv.size());

	for (int i = 0; i < int(pv.size()); i++) {
		printf("%d %d\n", pv[i].first, pv[i].second);
	}

	return 0;
}