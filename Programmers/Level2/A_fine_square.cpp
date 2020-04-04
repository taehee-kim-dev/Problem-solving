using namespace std;


// 최대공약수 구하는 함수
int gcd(int a, int b){

    while(b != 0){
        int r = a % b;
        a = b;
        b = r;
    }

    return a;
}

long long solution(int w,int h)
{
	long long answer = 0;

    // 최대공약수의 개수만큼 반복되는 사각형 구역이 생김
    long long number_of_repeating_common_square_sections = (long long)(gcd(w, h));

    // 하나의 반복되는 사각형 구역 안에서 갈라지는 1cm * 1cm 사각형의 개수는
    // 한 변의 길이 a + 다른 한 변의 길이 b - 1이다.
    // 왜냐하면 예를들어,
    // a >= b 라고 하자. 
    // 대각선으로 선을 그리면서 a변의 방향으로 나아갈 때,
    // 대각선이므로 동시에 b변의 방향으로도 나아가야 한다.
    // 하지만, b변의 방향으로 한 칸 이동할 때 마다
    // 하나의 추가적인 1cm * 1cm 사각형을 거쳐 가야 한다.
    // 따라서, 하나의 반복되는 사각형 구역 안에서 갈라지는 1cm * 1cm 사각형의 개수는
    // 한 변의 길이 a + 다른 한 변의 길이 b - 1이다.

    long long number_of_cracked_squares_in_one_repeating_common_square_section 
        = (w / number_of_repeating_common_square_sections) + (h / number_of_repeating_common_square_sections) - 1;
    
    // 전체 사각형의 개수 - ( 반복되는 사각형 구역의 개수 * 하나의 반복되는 사각형 구역 내에서 갈라지는 1cm * 1cm 사각형의 개수 )
    answer = (long long)(w) * (long long)(h) - (number_of_repeating_common_square_sections * number_of_cracked_squares_in_one_repeating_common_square_section);

	return answer;
}