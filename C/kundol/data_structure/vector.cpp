// Compile cmd in Terminal : 
// g++ -std=c++14 -Wall a.cpp -o test.out
// Execution cmd : 
// ./test.out

// 동적 배열로, Array와는 다르다. Array는 크기가 정해져있으나,
// vector의 경우 크기가 정해져있지 않다. (정확히는 정해져있지만, 자동으로 늘어남)

// vector<type> var1;


#include <bits/stdc++.h>
using namespace std;
vector<int> v;
vector<int> v2(5, 100);  //static allocation
vector<int> v3{10, 20, 30, 40, 50};

// 아래 v_2d, v_2d_3의 2차원 벡터는 같음 (v_2d는 push_back으로 직접 10번 넣어줌)
vector<vector<int>> v_2d;
vector<vector<int>> v_2d_2(10, vector<int>(10, 0));
vector<int> v_2d_3[10];


int main(){
    ios_base::sync_with_stdio(false);  // printf, scanf 등과의 동기화 해제로, 실행속도 더 빠를게
    cin.tie(NULL);
    cout.tie(NULL);

    for(int i=1; i<=10; i++)v.push_back(i);
    for(int a:v) cout << a << " ";
    cout << "\n";

    v.pop_back();

    for(int a:v) cout << a << " ";
    cout << "\n";

    v.erase(v.begin(), v.begin() + 3);

    for(int a:v) cout << a << " ";
    cout << "\n";

    auto a = find(v.begin(), v.end(), 100);
    if (a == v.end()) cout << "not found\n";

    fill(v.begin(), v.end(), 10);
    for(int a:v) cout << a << " ";
    cout << "\n";

    v.clear();
    cout << "아무것도 없을까?\n";
    for(int a:v) cout << a << " ";
    cout << "\n";

    for(int a:v2) cout << a << " ";
    cout << "\n";

    for(int a:v3) cout << a << " ";
    cout << "\n";

    for (int i=0; i<10; i++){
        vector<int> temp;
        v_2d.push_back(temp);
    }

    return 0;
}


