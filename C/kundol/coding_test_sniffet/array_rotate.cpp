#include <bits/stdc++.h>
using namespace std;
int main()
{
    // 한칸
    vector<int> v = {1, 2, 3, 4, 5, 6};
    rotate(v.begin(), v.begin() + 1, v.end());
    for (int i : v)
        cout << i << " ";
    cout << endl;
    // 2칸
    v = {1, 2, 3, 4, 5, 6};
    rotate(v.begin(), v.begin() + 2, v.end());
    for (int i : v)
        cout << i << " ";
    cout << endl;
    // 부분
    v = {1, 2, 3, 4, 5, 6};
    rotate(v.begin() + 1, v.begin() + 2, v.begin() + 5);
    for (int i : v)
        cout << i << " ";
    cout << endl;
    // 반대로
    v = {1, 2, 3, 4, 5, 6};
    rotate(v.rbegin() + 1, v.rbegin() + 2, v.rend()); // 첫째 인수와 두번째 인수 간의 차이만큼 회전합니다.
    for (int i : v)
        cout << i << " ";
    cout << endl;
}