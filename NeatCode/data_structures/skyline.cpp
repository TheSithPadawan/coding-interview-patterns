/*
lc link: https://leetcode.com/problems/the-skyline-problem/

Trick here is in sorting
each point there are two types of events: entering and exiting
in each type of event, the sort criteria is different;
to compare events across. prioritize entering than exiting
see how I define operator < here
*/


class Solution {
public:
    struct Element {
        int x;
        int y;
        bool start;
        Element(int x, int y, bool start) {
            this->x = x;
            this->y = y;
            this->start = start;
        }
        
        bool operator < (const Element & other) const {
            if (this->x != other.x) {
                return this-> x < other.x;
            }
            // prioritize entering event over exiting
            if (this->start != other.start) {
                if (this->start) return true;
                return false;
            }
            // both entering, prioritize taller buildings
            if (this->start && other.start) {
                // sort by height desc
                return this->y > other.y;
            }
            
            // both exiting, prioritize shorter buildings
            if (!this->start && !other.start) {
                // by height asc 
                return this->y < other.y;
            }
            // should not reach here
            return true;
        }
    };
    
    multiset <int> heights;
    
    int get_max_height() {
        if (heights.empty()) return 0;
        return *heights.rbegin();
    }
    vector<vector<int>> getSkyline(vector<vector<int>> & buildings) {
        vector <Element> points;
        for (const auto & b : buildings) {
            points.push_back(Element(b[0], b[2], true));
            points.push_back(Element(b[1], b[2], false));
        }
        sort(points.begin(), points.end());
      
        vector <vector<int>> results;
        for (const auto & e: points) {
            if (e.start) {
                if (e.y > get_max_height()) {
                    results.push_back({e.x, e.y});
                }
                heights.insert(e.y);
            } else {
                heights.erase(heights.equal_range(e.y).first);
                if (get_max_height() < e.y) {
                    results.push_back({e.x, get_max_height()});
                }
            }
        }
        return results;
    }
};