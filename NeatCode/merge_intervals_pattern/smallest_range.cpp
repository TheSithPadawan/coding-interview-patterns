/*
lc link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

k sorted list tells us about merge k pattern
each time pick min and max from the window, update the cover range
*/
class Solution {
public:
    struct Node {
      int val;
      int i;
      int list_id;
      Node () {};
      Node (int v, int id, int listid) {
          this->val = v;
          this->i = id;
          this->list_id = listid;
      }
      bool operator < (const Node & other) const {
          return val < other.val;
      }
    };
    vector<int> smallestRange(vector<vector<int>>& nums) {
        multiset <Node> ms;
        // populate
        vector <Node> nodes;
        for (int j = 0; j < nums.size(); ++j) {
            ms.insert(Node(nums[j][0], 0, j));
        }
        int start = 0, end = INT_MAX;
        while (ms.size() == nums.size()) {
            int s = ms.begin()->val;
            int e = ms.rbegin()->val;
            if (e - s < end - start) {
                start = s;
                end = e;
            }
            auto top = *ms.begin();
            if (top.i + 1 < nums[top.list_id].size()) {
                int nextindex = top.i + 1;
                ms.insert(Node(nums[top.list_id][nextindex], nextindex, top.list_id));
            }
            ms.erase(ms.begin());
        }
        return {start, end};
    }
};