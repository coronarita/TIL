#include <bits/stdc++.h>
using namespace std;

struct Point
{
    int y, x, z;
    Point(int y, int x, int z) : y(y), x(x), z(z) {}
    Point()
    {
        y = -1;
        x = -1;
        z = -1;
    }
    bool operator<(const Point &a) const
    {
        if (x == a.x)
        {
            if (y == a.y)
                return z < a.z;
            return y < a.y;
        }
        return x < a.x;
    }
};

int main()
{
    vector<Point> points;
    points.push_back({1, 2, 3});
    points.push_back({1, 1, 4});
    points.push_back({2, 1, 3});
    points.push_back({1, 2, 5});

    sort(points.begin(), points.end());
    for (Point p : points)
        cout << p.y << " " << p.x << " " << p.z << "\n";
    return 0;
}