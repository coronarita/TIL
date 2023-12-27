// linked list로, 요소가 인접한 메모리에 저장되지 않음.
// 순차적 접근만 가능하며, 각 요소들은 next/prev로 연결되어짐. 중복 허용
// 탐색 : O(n), 삽입/삭제는 O(1)
#include <bits/stdc++.h>
using namespace std;

class Node { 
public:
    int data;
    Node* next;
    Node(){
        data = 0;
        next = nullptr;
    }
    Node(int data){
        this->data = data;
        this->next = nullptr;
    }
};

void printList(Node* head){
    Node* current = head;
    while (current != nullptr){
        cout << current->data << " ";
        current = current->next;
    }
    cout << "\n";
}


int main(){
    // 노드 생성 및 초기화
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);

    printList(head);
    // 메모리 해제
    while (head != nullptr){
        Node* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}