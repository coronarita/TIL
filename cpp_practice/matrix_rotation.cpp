#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

#define N 10

int arr[N][N], temp_arr[N][N];

void init(){
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            arr[i][j] = i*10 + j;
}

void print_arr(){
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cout.width(2);
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

}

void rotate_r(){
    // Rotate array with 90 cw
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            temp_arr[i][j] = arr[N - j - 1][i];

}

void flip_axis(){
    // change x, y
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            temp_arr[i][j] = arr[j][i];
    
}
void rotate_l(){
    // rotate array with 90 ccw
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            temp_arr[i][j] = arr[j][N - i - 1];
    
}

void horizon(){
   for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            temp_arr[i][j] = arr[i][N - j - 1];
}
    
void vertical(){
    for (int i=0; i<N; i++)
            for (int j=0; j<N; j++)
                temp_arr[i][j] = arr[N - i - 1][j];
}

int main(){
    init();

    print_arr();

    //functional
    rotate_l();
    // flip_axis();
    // rotate_r();

    // copy value of array
    memmove(arr, temp_arr, sizeof(arr));
    print_arr();


    return 0;
}