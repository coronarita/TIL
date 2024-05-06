#include <bits/stdc++.h>
using namespace std;
queue<int> q;
int main(){
    for (int i=1; i<=10; i++)q.push(i);
    while(q.size()){
        cout << q.front() << "\n";
        q.pop();
    }

}