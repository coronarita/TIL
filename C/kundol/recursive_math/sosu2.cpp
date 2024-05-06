// sosu.cpp가 배열의 크기가 커질 경우 사용하기 힘들다.

#include <bits/stdc++.h>
using namespace std;
bool check(int n)
{
    if (n <= 1)
        return 0;
    if (n == 2)
        return 1;
    if (n % 2 == 0)
        return 0;
    for (int i = 3; i * i <= n; i++)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    for (int i = 1; i <= 20; i++)
    {
        if (check(i))
        {
            cout << i << "는 소수입니다.\n";
        }
    }
    return 0;
}