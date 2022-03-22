/*
lc link: https://leetcode.com/problems/sliding-window-median/

Two heap pattern
Here I used multiset (BST) instead of two heaps because removal in heap structure
is actually linear, not logrithmic. 

Other problems that can apply two-heap idea: Median in data stream
*/

class Solution {
public:
    multiset <int> maxheap;
    multiset <int> minheap;
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector <double> result;
        for (int i = 0; i < nums.size(); ++i) {
            if (maxheap.empty() || nums[i] <= *maxheap.rbegin()) {
                maxheap.insert(nums[i]);
            } else {
                minheap.insert(nums[i]);
            }
            rebalance();
            // move left most number out of the window
            if (i - k + 1 >= 0) {
                result.push_back(get_median());
                if (nums[i-k+1] <= *maxheap.rbegin()) {
                    auto itr = maxheap.find(nums[i-k+1]);
                    maxheap.erase(itr);
                } else {
                    auto itr = minheap.find(nums[i-k+1]);
                    minheap.erase(itr);
                }
            }
            rebalance();
        }
        
        return result;
    }
    
    void rebalance() {
        /* rebalance maxheap and minheap such that number
        of elements in maxheap is equal to or strictly greater than 
        number of elements in the minheap for 1 */
        if (maxheap.size() > minheap.size() + 1) {
            minheap.insert(*maxheap.rbegin());
            maxheap.erase(prev(maxheap.end()));
        } else if (minheap.size() > maxheap.size()) {
            maxheap.insert(*minheap.begin());
            minheap.erase(minheap.begin());
        }
    }
    
    double get_median() {
        if (maxheap.size() == minheap.size()) {
            return *maxheap.rbegin() / 2.0 + *minheap.begin() / 2.0;
        } else {
            return *maxheap.rbegin();
        }
    }
};