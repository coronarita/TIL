#include <bits/stdc++.h>
using namespace std;

struct Point
{
    int y, x;
    Point(int y, int x) : y(y), x(x) {}
    Point()
    {
        y = -1;
        x = -1;
    }
    bool operator<(const Point &a) const
    {
        if (x == a.x)
            return y < a.y;
        return x < a.x;
    }
};

int main()
{
    vector<Point> points;
    points.push_back(Point(1, 5));
    points.push_back(Point(3, 1));
    points.push_back(Point(2, 4));
    points.push_back(Point(2, 3));

    sort(points.begin(), points.end());

    for (const auto &point : points)
    {
        cout << "Point(" << point.y << ", " << point.x << ")\n";
    }

    return 0;
}