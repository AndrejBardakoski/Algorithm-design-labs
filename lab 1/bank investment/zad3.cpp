#include <iostream>
#include <vector>

using namespace std;

int matrix[50][50];
int MAX = 0;
int m, n;

int recursive(int level, int limit, int sum) {
    if (level >= m) {
        MAX = max(MAX, sum);
        return 0;
    }

    for (int i = 0; i <= limit; i++) {
        int current_sum = matrix[level][i] + sum;
        int current_limit = limit - i;
        int current_level = level + 1;
        cout << level << " " << limit << " " << sum;
        recursive(current_level, current_limit, current_sum);

    }
}

int main() {
    cin >> m >> n;

    for (int i = 0; i < m; i++) {
        matrix[i][0] = 0;
        for (int j = 1; j <= n; j++) {
            cin >> matrix[i][j];
        }
    }

    int dp[50][50];

    for (int j = 0; j <= n; j++) {
        dp[0][j] = matrix[0][j];
    }

    for (int i = 1; i < m; i++) {
        for (int j = 0; j <= n; j++) {
            dp[i][j] = 0;
            for (int k = 0; k <= j; k++) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + matrix[i][k]);

            }
        }
    }

    cout << dp[m - 1][n];

    return 0;
}
