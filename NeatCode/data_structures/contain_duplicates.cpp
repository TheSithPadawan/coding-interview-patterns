/*

lc link: https://leetcode.com/problems/contains-duplicate-iii/
just need to check the lower bound of the value range,
then verify the upper bound, if lower bound nums[i] - t does not satisfy
automatically the upper bound will not satisfy as well

maintain a window of size k

*/
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(t<0 || k<=0)
            return false;
        
        multiset <long> window;//window of size k
        for (int i = 0; i < nums.size(); ++i) {
            // first, delete elements that are not in the window
            if (i - k > 0) {
                window.erase((long) nums[i-k-1]);
            }
            
            // then recheck boundaries 
            auto low = window.lower_bound((long) nums[i] - t);
            
            if (low != window.end() && (*low - (long) nums[i]) <= t) {
                return true;
            }
            
            // add current value into the window
            window.insert((long) nums[i]);
        }
        return false;
    }
};