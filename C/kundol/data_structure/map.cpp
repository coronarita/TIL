#include <bits/stdc++.h>
using namespace std;

map<string, int> mp;
string a[] = {"주홍철", "이승철", "박종선"};

int main(){
    for (int i=0; i<3; i++){
        mp.insert({a[i], i+1}); // 키가 없다면 0으로 초기화하여 할당됨
        mp[a[i]] = i+1;
    }
    cout << mp["kundol"] << '\n';
    mp["kundol"] = 4;
    cout << mp.size() << '\n';
    mp.erase("kundol");
    auto it = mp.find("kundol"); // 참조만 해도 0으로 초기화
    if (it == mp.end()){
        cout << "못찾겠네 꾀꼬리\n";
    }
    mp["kundol"] = 100;

    it = mp.find("kundol");
    if (it != mp.end()){
        cout << (*it).first << " : " << (*it).second << '\n';
    }
    for (auto it: mp){ // 범위기반 for loop
        cout << (it).first << " : " << (it).second << '\n'; 
    }

    for (auto it = mp.begin(); it != mp.end(); it++){  // iterator를 사용(mp.begin,포인터)로 값에 접근
        cout << (*it).first << " : " << (*it).second << '\n';
    }
    mp.clear();


    return 0;
}