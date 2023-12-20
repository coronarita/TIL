#include <bits/stdc++.h>
using namespace std;
int main(void){
    int v[3] = {1, 2, 3};
    int a[3];
    memcpy(a, v, sizeof(v));
    cout << a[1] << endl;
    a[1] = 100;
    cout << a[1] << endl;
    cout << v[1] << endl;
}