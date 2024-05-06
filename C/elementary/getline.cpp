#include <bits/stdc++.h>
using namespace std;

int T;
string s;
int main(){
	cin >> T;
	string bufferflush;
	
	getline(cin, bufferflush); // remove space/enter char
	for (int i=0; i<T; i++){
		getline(cin, s);
		cout << s << endl;

	}		
	
	return 0;
}
