/*
lc link: https://leetcode.com/problems/time-based-key-value-store/
Yet another problem easily solved by using STL
upperbound: > 
lowerbound >=
*/

class TimeMap {
public:
    struct Node {
        string key;
        string value;
        int time;
        
      
        
        Node (string k, string v, int t) {
            key = k;
            value = v;
            time = t;
        }
        
        bool operator < (const Node & other) const {
            return this->time < other.time;
        }
    };
    
    unordered_map <string, multiset<Node>> store;
    
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        store[key].insert(Node(key, value, timestamp));
    }
    
    string get(string key, int timestamp) {
        auto & ms = store[key];
        auto itr = ms.upper_bound(Node("", "", timestamp));
        if (itr == ms.begin()) return "";
        auto itr2 = prev(itr);
        return itr2->value;
    }
};