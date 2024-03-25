#include <iostream>

using namespace std;

void func(int n, int arr[]){
    int B[200];
    for (int i = 0; i < 200; i++) {
        B[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        B[arr[i]]++;
    }
    for (int i = 0; i < n; i++) {
        if (B[i] > 1){
            cout << i <<" ";
        }
    }

}