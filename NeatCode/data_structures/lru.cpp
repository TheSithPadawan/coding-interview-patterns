#include <bits/stdc++.h>
#define int long long
#define  um unordered_map
#define us unordered_set
#define pq priority_queue
#define mod 1000000007
#define md 998244353
 
#define endl  "\n"
using namespace std; 

// LRU question: https://leetcode.com/problems/lru-cache/

// Pattern: store <key, iterator> in cpp unordered_map so we have direct access to list node

class LRUCache {
    // lru with ttl implementation: https://leetcode.com/playground/YjnCxVtU

public:
    struct Node {
        int key;
        int value;
        Node (int k, int v) {
            key = k;
            value = v;
        }
    };
    int cap;
    um <int, list<Node>::iterator> store;
    list <Node> order;
    LRUCache(int capacity) {
        this->cap = capacity;
    }

    int get(int key) {
      auto itr = store.find(key);
      if (itr == store.end()) return -1;
      int ans = itr->second->value;
      order.erase(itr->second);
      Node newnode = Node(key, ans);
      order.push_front(newnode);
      // note: cpp iterator assign to another value makes a copy
      // rather than direct reference, so the next time order has a pushfront
      // it does not affect store[key]
      store[key] = order.begin();
      return ans;
    }

    void put(int key, int value) {
        if (store.find(key) == store.end()) {
            if (store.size() + 1 <= cap) {
                // add
                auto newnode = Node(key, value);
                order.push_front(newnode);
                store[key] = order.begin();
            } else {
                // evict 
                auto evictnode = prev(order.end());
                int evictkey = evictnode->key;
                store.erase(evictkey);
                order.erase(evictnode);
                // then add
                auto newnode = Node(key, value);
                order.push_front(newnode);
                store[key] = order.begin();
            }
        } else {
            // update
            store[key]->value = value;
            get(key);
        }
    }

};


int32_t main() {
    LRUCache C = LRUCache(2);
    C.put(1, 1);
    C.put(2, 2);
    cout << C.get(1) << endl;
    C.put(3, 3);
    cout << C.get(2) << endl;
    cout << C.get(1) << endl;
    return 0;
}