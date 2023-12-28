// 등차수열
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n = 5;
    int ret = 0;
    for (int i = 1; i <= n; i++)
    {
        ret += i;
    }
    cout << ret << endl;
    cout << n * (n + 1) / 2 << endl; // 공식을 쓰면 O(n)이 아니라 O(1)만에 계산이 가능하다.

    int a = 3, l = 23;
    cout << n * (a + l) / 2 << endl;

    cout << "--------\n";
    cout << "등비수열의 합 구하기 : {1, 2, 4, 8}" << endl;
    a = 1, n = 4;
    int r = 2;
    vector<int> v;
    cout << a * ((int)pow(r, n) - 1) / (r - 1); // pow는 부동소수점을 가진 double type을 받고 반환해준다.
    cout << endl;

    for (int i = 0; i < n; i++)
    {
        v.push_back(a);
        a *= r;
    }
    for (int i : v)
        cout << i << ' ';

    cout << accumulate(v.begin(), v.end(), 0);

    return 0;
}