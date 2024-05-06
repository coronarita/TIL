#include <bits/stdc++.h>
using namespace std;
// 정렬이 되지 않은 map임

/*
map : 정렬이 됨 / 레드블랙트리 기반 / 탐색,삽입,삭제에 O(logN)
unordered_map : 정렬이 안됨 / 해시테이블 기반 / 탐색,삽입,삭제에
O(1), 최악의 경우 O(N)
*/
unordered_map<string, int> umap;

int main(){
    umap["bcd"] = 1;
    umap["aaa"] = 1;
    umap["aba"] = 1;
    
    for(auto it : umap){
        cout << it.first << " " << it.second << '\n';
    }
}