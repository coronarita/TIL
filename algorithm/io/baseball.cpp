/*
⚾는 9명으로 이루어진 두 팀이 공격과 수비를 번갈아 하는 게임이다.
하나의 이닝은 공격과 수비로 이루어져 있고, 총 N이닝 동안 게임을 진행해야 한다.
한 이닝에 3아웃이 발생하면 이닝이 종료되고, 두 팀이 공격과 수비를 서로 바꾼다.

두 팀은 경기가 시작하기 전까지 타순(타자가 타석에 서는 순서)을 정해야 하고,경기 중에는 타순을 변경할 수 없다.
9번 타자까지 공을 쳤는데 3아웃이 발생하지 않은 상태면 이닝은 끝나지 않고, 1번 타자가 다시 타석에 선다.
타순은 이닝이 변경되어도 순서를 유지해야 한다. 예를 들어, 2이닝에 6번 타자가 마지막 타자였다면, 
3이닝은 7번 타자부터 타석에 선다.

공격은 투수가 던진 공을 타석에 있는 타자가 치는 것이다. 공격 팀의 선수가 1루, 2루, 3루를 거쳐서 홈에
도착하면 1점을 득점한다. 타자가 홈에 도착하지 못하고 1루, 2루, 3루 중 하나에 머물러있을 수 있다.
루에 있는 선수를 주자라고 한다. 이닝이 시작될 때는 주자는 없다.
타자가 공을 쳐서 얻을 수 있는 결과는 안타, 2루타, 3루타, 홈런, 아웃 중 하나이다.
각각이 발생했을 때, 벌어지는 일은 다음과 같다.

안타: 타자와 모든 주자가 한 루씩 진루한다.
2루타: 타자와 모든 주자가 두 루씩 진루한다.
3루타: 타자와 모든 주자가 세 루씩 진루한다.
홈런: 타자와 모든 주자가 홈까지 진루한다.
아웃: 모든 주자는 진루하지 못하고, 공격 팀에 아웃이 하나 증가한다.

한 야구팀의 감독 아인타는 타순을 정하려고 한다. 
아인타 팀의 선수는 총 9명이 있고, 1번부터 9번까지 번호가 매겨져 있다. 
아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다.
이제 다른 선수의 타순을 모두 결정해야 한다. 아인타는 각 선수가 각 이닝에서 어떤 결과를 얻는지 
미리 알고 있다. 가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.
*/

#include <iostream>
#include <vector>

using namespace std;

const int PLAYER_COUNT = 9;
const int BASE_COUNT = 4;
int n;
int maxPoint = 0;
// 이중 리스트 유사
vector<vector<int>> innings;

void input() {
	cin >> n;

	int temp;
	for (int i = 0; i < n; i++) {
		vector<int> player;
		for (int j = 0; j < PLAYER_COUNT; j++) {
			cin >> temp;
			player.push_back(temp);
		}
		innings.push_back(player);
	}
}

void output() {
	cout << maxPoint << endl;
}

void setMaxPoint(int point) {
	if (point > maxPoint) {
		maxPoint = point;
	}
}

void clearBase(bool base[BASE_COUNT]) {
	for (int i = 0; i < BASE_COUNT; i++) {
		base[i] = false;
	}
}

int runBase(bool base[BASE_COUNT], int run) {
	int point = 0;
	base[0] = true;

	while (run > 0) {
		run--;

		for (int i = BASE_COUNT - 1; i >= 0; i--) {
			if (base[i]) {
				base[i] = false;
				(i + 1 < BASE_COUNT) ? base[i + 1] = true : point++;
			}
		}
	}

	return point;
}

int getPoint(const vector<int> index) {
	int point = 0;
	int pointer = 0;
	int out = 0;

	bool base[BASE_COUNT];

	for (int i = 0; i < n; i++) {
		out = 0;
		clearBase(base);

		while (out < 3) {
			int player = innings[i][index[pointer]];
			switch (player)
			{
			case 0:
				out++;
				break;
			default:
				point += runBase(base, player);
				break;
			}

			pointer = (pointer + 1) % PLAYER_COUNT;
		}
	}

	return point;
}

void makeTeamIndex(const vector<int> in, const vector<int> remain) {
	vector<int> inCopy;
	vector<int> remainCopy;

	//4번 타자 세팅
	if (in.size() == 3) {
		inCopy.assign(in.begin(), in.begin() + in.size());
		inCopy.push_back(0);

		makeTeamIndex(inCopy, remain);
	}
	//4번 이외의 순서 세팅
	else if (remain.size() > 0) {
		for (int i = 0; i < remain.size(); i++) {
			inCopy.assign(in.begin(), in.begin() + in.size());
			remainCopy.assign(remain.begin(), remain.begin() + remain.size());

			inCopy.push_back(remainCopy[i]);
			remainCopy.erase(remainCopy.begin() + i);

			makeTeamIndex(inCopy, remainCopy);
		}
	}
	//세팅 완료
	else {
		setMaxPoint(getPoint(in));
		return;
	}
}

int main() {
	input();

	vector<int> inCopy;
	vector<int> remainCopy;
	for (int i = 1; i < PLAYER_COUNT; i++) {
		remainCopy.push_back(i);
	}

	makeTeamIndex(inCopy, remainCopy);

	output();
}
​
[출처] [백준 17281번] ⚾(야구 게임)|작성자 eddy1001