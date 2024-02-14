class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); ++i) {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                count++;
                l--;
                r++;
            }

            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                count++;
                l--;
                r++;
            }
        }

        return count;
    }
};

// this is the same question as longest palindrome
// lc link: https://leetcode.com/problems/palindromic-substrings/
