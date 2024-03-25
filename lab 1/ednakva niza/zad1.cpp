#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    int A[50];
    int B[50];

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    int sum_min = 999999999;


    for (int shift = 0; shift < n; shift++) {
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int shifted_i = i + shift;
            if (shifted_i >= n)
                shifted_i -= n;
            sum += abs(A[i] - B[shifted_i]);
        }
        sum += shift;
        if (sum < sum_min) {
            sum_min = sum;
        }
    }

    cout << sum_min;

    return 0;
}
