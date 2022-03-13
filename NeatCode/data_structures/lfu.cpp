#include <bits/stdc++.h>
#define int long long
#define  um unordered_map
#define us unordered_set
#define pq priority_queue
#define mod 1000000007
#define md 998244353
 
 
 
#define endl  "\n"
using namespace std; 

// lc question link: https://leetcode.com/problems/lfu-cache/

struct Node {
    int value;
    int time;
    int count;
    int key;
    Node (int k, int v, int t, int c) {
        value = v;
        time = t;
        count = c;
        key = k;
    }

    bool operator == (const Node & other) const {
        return this->key == other.key;
    }

    bool operator < (const Node & other) const {
        if (this->count == other.count) {
            return this->time < other.time;
        }
        return this->count < other.count;
    }
};

class LFUCache {
public:
    int cap;
    int time;
    um <int, multiset<Node>::iterator> store;
    //
    multiset <Node> freq;
    // constructor 
    LFUCache(int capacity) {
        cap = capacity;
        time = 0;
    }
    
    int get(int key) {
        time++;
        if (store.empty() || store.find(key) == store.end()) return -1;
        // update time, update count
        auto node = store[key];
        int value = node->value;
        int count = node->count + 1;
        freq.erase(node);
        Node newnode = Node(key, value, time, count);
        auto itr = freq.insert(newnode);
        store[key] = itr;
        return value;
    }
    
    void put(int key, int value) {
          time++;
          if (cap == 0) return;
          auto itr = store.find(key);
          if (itr == store.end()) {
              // add
              if (store.size() + 1 > cap) {
                  // evict then add
                  auto evictnode = freq.begin();
                  int evictkey = evictnode->key;
                  store.erase(evictkey);
                  freq.erase(evictnode);
                  add_element(key, value, time, 1);
              } else {
                  // add no evict
                  add_element(key, value, time, 1);
              }

          } else {
              // perform update = delete then add
              int newcount = itr->second->count + 1;
              freq.erase(store[key]);
              store.erase(itr);
              add_element(key, value, time, newcount);
          }
    }
    
    void add_element(int key, int value, int curtime, int curfreq) {
       auto newnode = Node(key, value, curtime, curfreq);
       auto itr = freq.insert(newnode);
       store[key] = itr;
    }
};

int32_t main() {
    LFUCache * obj = new LFUCache(2);
    obj->put(1, 1);
    obj->put(2, 2);
    cout << obj->get(1) << endl;
    obj->put(3,3);
    cout << obj->get(2) << endl;
    cout << obj->get(3) << endl;
    obj->put(4, 4);
    cout << obj->get(1) << endl;
    cout << obj->get(3) << endl;
    cout << obj->get(4) << endl;
    return 0;
}