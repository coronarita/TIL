#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout << "정렬되지 않은 배열 기반\n";
    int a[] = {1, 3, 2};
    do
    {
        for (int i : a)
            cout << i << " ";
        cout << endl;
    } while (next_permutation(a, a + 3)); // 원래는 배열의 주소가 들어가야 하지만, pointer to decay 가 배열의 이름에서 일어나서 사용 가능
    cout << endl;
    cout << "정렬된 배열 기반\n";
    int b[] = {1, 2, 3};
    do
    {
        for (int i : b)
            cout << i << " ";
        cout << endl;
    } while (next_permutation(b, b + 3));

    return 0;
}