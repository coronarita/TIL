// 연결리스트는 벡터, 배열과 달리 k번째 요소를 접근 할 때 O(k)이 걸림
// 삽입/삭제에는 O(1)이 걸림, 삽입/삭제가 많을 때 사용하는 것이 좋다.

#include <bits/stdc++.h>
using namespace std;
list<int> a;
void print(list<int> a){
    for (auto it: a) cout << it <<" ";
    cout << "\n";
}

int main(){
    for (int i=1; i<=3; i++)a.push_back(i); // 1 2 3
    for (int i=1; i<=3; i++)a.push_front(i); // 3 2 1 1 2 3

    auto it = a.begin(); it++;
    a.insert(it, 1000);
    print(a);

    it = a.begin(); it++;
    a.erase(it);
    print(a);

    a.pop_front();
    a.pop_back();
    print(a);

    cout << a.front() << " : " << a.back() << '\n';
    a.clear();
    return 0;
}