#include <iostream>

using namespace std;

char s[35] = "A man, a plan, a canal: Panama";

bool isPalindrome(char *s){
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for (int i = 0; i<str_len; i++){
        // skip pointer 처리
        while (!isalnum(s[i+bias_left])){ // 숫자나 알파벳이 아니라면, 
            bias_left++; // 다음 칸으로 스킵
            if (i + bias_left == str_len)
                return true;
        }

        while (!isalnum(s[str_len - i - bias_right])){
            bias_right++;
        }

        if (i + bias_left >= str_len - i - bias_right)
            break;
        
        // 팰린드롬 비교
        
        if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
            return false;
    }
    return true;
}


int main(){
    bool a;
    a = isPalindrome(s);
    cout << "Palindrome checker :" << a << endl;
    cout << "finish";
    return 0;
}
