
// Compile cmd in Terminal :
// g++ -std=c++14 -Wall a.cpp -o test.out
// Execution cmd :
// ./test.out

#include <bits/stdc++.h>
using namespace std;

vector<string> split(string input, string delimiter)
{
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos)
    {
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

int main()
{
    string s = "안녕하세요 저는 지금 실업급여 관련 온라인 교육을 수강중입니다!", d = " ";
    vector<string> a = split(s, d);
    for (string b : a)
        cout << b << endl;
    return 0;
}
