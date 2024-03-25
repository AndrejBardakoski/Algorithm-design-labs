#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int i = 1;
    while (i * (i + 1) / 2 < n) {
        i++;
    }

    cout << n - (i - 1) * i / 2;

    return 0;
}
