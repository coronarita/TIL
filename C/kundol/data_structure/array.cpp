
#include <bits/stdc++.h>
using namespace std;

int a[3] = {1,2,3};
int a2[] = {1,2,3,4};
int a3[10];

const int mxy = 3;
const int mxx = 4;
int b[mxy][mxx];

int main(){

    for (int i=0; i<mxy; i++){
        for (int j=0; j<mxx; j++){
            b[i][j] = (i+j);
        }
    }
    // good
    for (int i=0; i<mxy; i++){
        for (int j=0;j<mxx; j++){
            cout << b[i][j] <<' ';
        }
        cout << '\n';
    }

    // bad
    for (int i=0; i<mxx; i++){
        for (int j=0; j<mxy; j++){
            cout << b[j][i] << ' ';
        }
        cout << '\n';
    }


    for (int i=0;i<3;i++) cout << a[i] << " ";
    cout << '\n';
    for (int i: a) cout << i << " ";

    for (int i=0; i<4; i++) cout << a2[i] << " ";
    cout << "\n";
    for (int i: a2) cout << i << " ";
    cout << '\n';
    for (int i=0; i<10; i++) a3[i] = i;
    for (int i: a3) cout << i << " ";
    return 0;



}