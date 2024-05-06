// 직접 구현
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {1, 2, 3, 4, 5, 6};
    int i = 1;
    int temp = v[i];
    v[i] = v[i + 1];
    v[i + 1] = v[i + 2];
    v[i + 2] = v[i + 3];
    v[i + 3] = temp;
    // v[i + 3] = v[i + 4];
    // v[i + 4] = v[i + 5];
    for (int i : v)
        cout << i << " ";

    return 0;
}