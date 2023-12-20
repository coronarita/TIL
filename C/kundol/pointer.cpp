#include <bits/stdc++.h>
using namespace std;
int i;
string s = "kundol";
int main(){
    i = 0;
    int *a = &i;
    cout << a << endl;
    string *b = &s;
    cout << b << endl;
    cout << sizeof(a) << endl;
    return 0;
}