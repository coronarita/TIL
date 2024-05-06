// 1. 지역변수 보다는 전역변수를,
// 변수명은 간결하게 (ex, result - res, count - cnt)
// 2. 배열은 넓게 - 오버플로에 대한 신경을 덜 쓰게 int a[10004];로 최대범위보다 3~4개 여유있게 만들기
// 3. 초기값은 답의 범위 밖에서 찾기 - 초기화 시 답의 범위에서 지정하면, 우연히 맞을 수가 있고, 반대로 맞왜틀에 걸릴수도 있다.
// 4. 타자연습 (typingtest.com 45wpm 이상), test해 보니 67~85 wpm이 나오고 평균 72wpm이 나오는 것을 확인할 수 있었다.
// 5. define으로 예약된 변수명희석화
// 예 : #define time aaa
//     int time[4];

// 6. 입출력싱크 : sync_with_stdio(false) / cin.tie(0) -> printf, scanf, cin , cout간의 싱크를 맞추기 위함이라는데,
// 이거 해제 해줘서 시간초과 통과하는 경우도 있다고 한다.
// 7. endl 대신 개행문자('\n') 쓰기 : endl 은 버퍼플러시가 달려있어서 조금 더 시간이 소요된다고 한다.
// 8. Stack overflow
// 9. variables Initialiation
// 10. The accuracy of float type -> using double and the gap when calculating equal
// 11. string with char -> considering null char
// 12. reference error : pop, top 쓸 때, size가 있는지 ?
// 13. UB :
// 14. 끝을 정하지 않은 경우 : cin >> n

#include <bits/stdc++.h>
using namespace std;
// int tree[10000000]; 문제없이 잘 됨
int a, b, c;

int main()
{
    a = 2;
    // int tree[10000000]; // 지역변수로 이렇게 하면 segmentation fault가 발생함
    cout << a << " : " << b << " : " << c << endl;
    /*
    지역변수는 stack에 쓰레기값으로 초기화되어 할당되는 반면, 전역변수는 0으로 초기화되어서
    bss segment / data segment에 들어감.
    stack에 쌓이면 메모리 제한이 걸림. 많은 배열 선언에 장애가 됨
    */

    return 0;
}