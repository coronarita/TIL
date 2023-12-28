#include <bits/stdc++.h>
using namespace std;
int cnt = 0;
int fibo(int n)
{
    cout << "fibo:" << n << endl;
    cnt++;
    if (n == 0 || n == 1)
        return n;
    return fibo(n - 1) + fibo(n - 2);
}
int n = 5;
int main()
{
    cout << fibo(5) << endl;
    cout << cnt << endl;
    return 0;
}
