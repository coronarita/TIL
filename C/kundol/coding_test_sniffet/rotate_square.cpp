#include <bits/stdc++.h>
using namespace std;

void rotate_square_cw(vector<vector<int>> &key)
{
    //  n x n 사각형을 회전합니다.
    int n = key.size();
    vector<vector<int>> temp(n, vector<int>(n, 0)); // 구체적인 차원까지 묘사 해 줘야 함

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            temp[i][j] = key[n - j - 1][i];
        }
    }

    key = temp;
    return;
}

void printV(vector<vector<int>> key)
{
    for (int i = 0; i < key.size(); i++)
    {
        for (int j = 0; j < key.size(); j++)
        {
            cout << key[i][j] << " ";
        }
        cout << endl;
    }
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<vector<int>> v = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    };

    printV(v);
    cout << "------" << endl;
    rotate_square_cw(v);
    printV(v);
    return 0;
}