#include <bits/stdc++.h>
using namespace std;
int a[3] = {1,2,3};
int main(){
    // the name of static array - binding the address 
    int *c = a;
    cout << c << endl;
    cout << &a[0] << endl;
    cout << c+1 << endl;
    cout << &a[1] << endl;
    return 0;
}