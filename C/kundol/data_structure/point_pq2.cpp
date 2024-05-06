#include <bits/stdc++.h>
using namespace std;
struct Point
{
    int y, x;
};
struct cmp
{
    bool operator()(Point a, Point b)
    {
        return a.x > b.x; // 최소 힙, a.x > b.x 가 참(크다면) a는 우선순위가 '낮다'. 큰게 우선순위가 낮다 -> 최소 힙 !! a가 작을 때 우선순위가 높다 : 힙의 상단에 위치한다. :
        //
        // return a.x < b.x; // 최대 힙 :
    }
};

priority_queue<Point, vector<Point>, cmp> pq;

int main()
{
    pq.push({1, 1});
    pq.push({2, 2});
    pq.push({3, 3});
    pq.push({4, 4});
    pq.push({5, 5});
    pq.push({6, 6});
    cout << pq.top().x << "\n";
    return 0;
}