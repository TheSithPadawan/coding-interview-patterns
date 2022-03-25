/*
lc link: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

This is a dfs version, good enough for most companies
//todo: memo version
*/
class Solution {
public:
    int curmin;
    int minSessions(vector<int>& tasks, int sessionTime) {
        // in each task make decision: 
        // backtracking solution
        // (1) include it in existing session if possible 
        // (2) if not possible, make a new session 
        sort(tasks.begin(), tasks.end());
        vector <int> curr;
        curmin = tasks.size();
        solve(tasks, sessionTime, curr, 0);
        return curmin;
    }
    
    void solve(const vector <int> & tasks, int time, vector <int> & curr, int index) {
        // pruning. passed lc but perhaps due to weak test cases
        if (curr.size() > curmin) return;
        
        if (index == tasks.size()) {
            curmin = min(curmin, (int) curr.size());
            return;
        }
        
        // add to existing session
        for (int i = 0; i < curr.size(); ++i) {
            if (curr[i] + tasks[index] <= time) {
                curr[i] += tasks[index];
                solve(tasks, time, curr, index + 1);
                // backtrack
                curr[i] -= tasks[index];
            }
        }
        // create a new session
        curr.push_back(tasks[index]);
        solve(tasks, time, curr, index + 1);
        curr.pop_back();
    } 
};