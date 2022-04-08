/**
lc link: https://leetcode.com/problems/perfect-squares/

same pattern as coin change.  unbounded knapsack
py times out so provide cpp
**/

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, -1);
        dp[0] = 0;
        dp[1] = 1;
        
        return memo(n, dp);
    }
    
    int memo(int n, vector <int> & dp) {
        if (dp[n] != -1) return dp[n];
        
        dp[n] = INT_MAX;
        for (int i = 1; i < n; ++i) {
            if (i * i > n) break;
            dp[n] = min(dp[n], memo(n - i*i, dp) + 1);
        }
        return dp[n];
    }
};