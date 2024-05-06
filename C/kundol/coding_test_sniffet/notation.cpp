#include <bits/stdc++.h>
using namespace std;
vector<int> v;

int main()
{
    int n = 100;
    int b = 2;
    while (n > 1)
    {
        v.push_back(n % b); // 나머지를 주워담음
        n /= b;
    }
    if (n == 1)
        v.push_back(1);
    reverse(v.begin(), v.end());
    for (int a : v)
    {
        // 10진법 이상일 때 변환
        if (a >= 10)
            cout << char(a + 55);
        else
            cout << a;
    }
    return 0;
}
