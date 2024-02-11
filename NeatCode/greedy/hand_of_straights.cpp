class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) return false;
        multiset<int> ms (hand.begin(), hand.end());
        int numGroup = hand.size() / groupSize;
        for (int i = 0; i < numGroup; ++i) {
            int cur = *ms.begin();
            ms.erase(ms.begin());
            int count = 1;
            while (count < groupSize) {
                // no consecutive
                auto it = ms.find(cur + 1);
                if (it == ms.end()) return false;
                ms.erase(it);
                cur = cur + 1;
                count++;
            }
        }
        return true;
    }
};
// in cpp multiset erase(value) removes all occurrences
// while erase(iterator) removes a specific occurrence
// lc link: https://leetcode.com/problems/hand-of-straights/
// time complexity: bounded by n lgn
