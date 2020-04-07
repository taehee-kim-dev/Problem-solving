#include <string>
#include <vector>

using namespace std;

int solution(string arrangement) {
    int answer = 0; // 잘린 쇠막대기 조각의 총 개수

    int layer = 0; // 현재 쇠막대기를 겹친 층 수

    for(int i = 0; i < arrangement.length(); i++){

        switch (arrangement[i]){
            case '(':
                // 현재 검사하는 문자가 '('라면,
                switch (arrangement[i + 1]){
                    // 다음 문자 검사
                    // 맨 마지막 문자가 '('일 수는 없으므로,
                    // arrangement[i + 1]는 안전한 범위이다.
                    case '(':
                        // 다음 문자가 '('라면, 현재 검사한 것은 쇠막대기의 시작부분 이므로
                        // 쇠막대기를 겹친 층 수를 1 증가시킨다.
                        layer++;
                        break;
                    case ')':
                        // 다음 문자가 ')'라면 레이저
                        // 현재 층 만큼 잘려나갈 것이므로, answer에 layer를 추가한다.
                        answer += layer;
                        // 다음 문자까지 어차피 레이저이므로, i값을 1 증가시킨다.
                        i++;
                        break;
                }

                break;
            case ')':
                // 현재 검사하는 문자가 ')'라면, 쇠막대기의 끝이므로
                // answer을 1 증가시키고, layer을 1 감소시킨다.
                answer++;
                layer--;
                break;
        }
    }

    return answer;
}