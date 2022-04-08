"""
lc link: 
https://leetcode.com/problems/stock-price-fluctuation/

pattern: cpp map -> multiset node iterator coding pattern
same question as lru cache
"""
class StockPrice {
public:
    struct Node {
        int time;
        int price;
        Node (int t, int p) {
            time = t;
            price = p;
        }
        Node () {};
        
        bool operator < (const Node & other) const {
            return this->price < other.price;
        }
    };
    // tracking time
    map <int, multiset<Node>::iterator> tmap;
    // tracking price
    multiset <Node> pset;
    
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        auto itr = tmap.find(timestamp);
        if (itr != tmap.end()) {
            pset.erase(tmap[timestamp]);
        } 
        auto itr2 = pset.insert(Node(timestamp, price));
        tmap[timestamp] = itr2;
    }
    
    int current() {
        auto pair = tmap.rbegin();
        return pair->second->price;
    }
    
    int maximum() {
        auto itr = pset.rbegin();
        return itr->price;
    }
    
    int minimum() {
        auto itr = pset.begin();
        return itr->price;
    }
};