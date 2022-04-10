"""
lc link: https://leetcode.com/problems/sliding-window-maximum/

coding pattern: deque
delete useless stuff from existing data before adding new ones
"""

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque <int> deq;
        vector <int> result;
        for (int i = 0; i < nums.size(); ++i) {
            // 1. delete from the front where index < i - 2
            while (!deq.empty() && deq.front() <= i - k) {
                deq.pop_front();
            }
            
            // 2. delete from the back
            while (!deq.empty() && nums[deq.back()] <= nums[i]) {
                deq.pop_back();
            }
            
            // push 
            deq.push_back(i);
            // output answer
            if (i - k + 1 >= 0) {
                result.push_back(nums[deq.front()]);
            }
        }
        
        return result;
    }
};