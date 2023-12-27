#include <bits/stdc++.h>
using namespace std;

map<int, int> mp;
map<string, string> mp2;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    // cout << mp[1] << '\n';  // 0
    // cout << mp2["aaa"] << '\n'; // 공백

    // if (mp[1] == 0){ // 이미 0이 할당되어버림
    //     mp[1] = 2;
    // }

    if (mp.find(1) == mp.end()){ // find를 사용하면 할당되지 않음
        mp[1] = 2;
    }

    for (auto i : mp) cout << i.first << " " << i.second;
    cout << '\n';
    for (auto i : mp2) cout << i.first << " " << i.second;
    
    return 0;
}