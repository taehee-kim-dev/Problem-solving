#include <iostream>

using namespace std;


// ��ü �� ����
char map[2200][2200];

// �� �ʱ�ȭ
void InitMap(int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			map[i][j] = ' ';
		}
	}
}


// �¿���� ��ǥȭ �Ͽ� 3��о� ��������
void DecideDot(int n, int x, int y) {
	if (n == 1) {
		map[x][y] = '*';
		return;
	}

	int div = n / 3;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (i == 1 && j == 1)
				continue; // ��� ��ŵ

			DecideDot(div, x + (div * i), y + (div * j));
		}
	}
	return;
}



int main_2447(void) {

	int n;

	cin >> n;

	InitMap(n);
	DecideDot(n, 0, 0);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << map[i][j];
		}
		cout << endl;
	}

	return 0;
}