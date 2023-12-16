#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main()
{
    vector<int> a{1, 2, 3, 3, 3, 4};

    cout << &*lower_bound(a.begin(), a.end(), 3) << endl;
    cout << &*a.begin() << endl;
    cout << &*(a.begin() + 1) << endl;
    cout << &*(a.begin() + 2) << endl;

    cout << lower_bound(a.begin(), a.end(), 3) - a.begin() << endl;
    cout << upper_bound(a.begin(), a.end(), 3) - a.begin() << endl;

    vector<int> b{0, 0, 0, 0};
    cout << &*(b.begin() + 3) - &*b.begin() << endl;
}
