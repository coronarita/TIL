#include <bits/stdc++.h>
using namespace std;
int main(){
    string a = "abcda";
    string *b = &a;
    cout << b << endl;
    cout << *b << endl;
}