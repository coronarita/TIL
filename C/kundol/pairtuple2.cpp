#include <bits/stdc++.h>
using namespace std;
pair<int, int> pi;
tuple<int, int, int> tl;
int a, b, c;

int main(){
    pi = {1, 2};
    a = pi.first;
    b = pi.second;
    cout << a << " : " << b << endl;

    tl = make_tuple(1, 2, 3);
    a = get<0>(tl);
    b = get<1>(tl);
    c = get<2>(tl);

    cout << a << " : " << b << " : " << c << endl;
    return 0;

}