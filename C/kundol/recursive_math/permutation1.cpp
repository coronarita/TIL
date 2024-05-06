#include <bits/stdc++.h>

// I'll using next_permutation and prev_permutation
using namespace std;

void printV(vector<int> &v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}

int main()
{
    int a[3] = {1, 2, 3};
    vector<int> v;

    for (int i = 0; i < 3; i++)
        v.push_back(a[i]);
    // 1, 2, 3부터 오름차순으로 순열을 뽑습니다. 개인적으로는 제일 간단한 것 같은데
    do
    {
        printV(v);                                  // 출력하고
    } while (next_permutation(v.begin(), v.end())); // 순서를 바꿔서 뽑아주는 것 같은데, 종료조건까지 있는 것 같다.
    cout << "----------------\n";
    v.clear();
    for (int i = 2; i > -1; i--)
        v.push_back(a[i]);
    do
    {
        printV(v);                                  // 출력하고
    } while (prev_permutation(v.begin(), v.end())); // 순서를 바꿔서 뽑아주는 것 같은데, 종료조건까지 있는 것 같다.

    cout << "----------------\n";
    do
    {
        printV(v);                                        // 출력하고
    } while (prev_permutation(v.begin(), v.begin() + 2)); // 배열의 x번째 (0,1,2) 순서를 컨트롤 (인덱스 범위)

    return 0;
    // 각 함수를 쓸 떄, next_permutation은 오름차순, prev_permutation은 내림차순으로 각각 정렬 후에 사용하는 것이 필요하다. 중요!
}