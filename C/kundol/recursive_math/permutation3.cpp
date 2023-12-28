#include <bits/stdc++.h>
// 재귀를 활용하여 순열 구현
using namespace std;
int a[3] = {1, 2, 3};
int n = 3, r = 3; // r 바꿔보기
void print()
{
    for (int i = 0; i < r; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

void makePermutation(int n, int r, int depth)
{
    if (r == depth)
    {
        print();
        return;
    }

    for (int i = depth; i < n; i++)
    {
        cout << i + 1 << " : " << depth + 1 << "를 바꾼다" << endl;
        swap(a[i], a[depth]);
        makePermutation(n, r, depth + 1);
        cout << i + 1 << " : " << depth + 1 << "를 다시 바꾼다" << endl;
        swap(a[i], a[depth]);
    }
    return;
}

int main()
{
    makePermutation(n, r, 0);
    return 0;
}