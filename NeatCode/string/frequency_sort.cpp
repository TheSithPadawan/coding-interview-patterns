/*
A bucket sort solution
https://leetcode.com/problems/sort-characters-by-frequency/
*/

class Solution {
public:
    string frequencySort(string s) {
        unordered_map <char, int> ump;
        for (char ch: s){
            ump[ch]++;
        }
        int max_cnt = INT_MIN;
        for (auto [a, b]: ump){
            max_cnt = max(b, max_cnt);
        }
        vector <vector<char>> buckets(max_cnt + 1);
        for (auto [a, b]: ump){
            buckets[b].push_back(a);
        }
        string ans;
        for (int i = max_cnt; i >= 0; i--){
            for (auto ch: buckets[i]){
                for (int j = 0; j < i; j++){
                   ans += ch;
                }
            }
        }
        return ans;
    }
};