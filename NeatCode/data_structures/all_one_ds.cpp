// lc link: https://leetcode.com/problems/all-oone-data-structure

// Flex: 100 ms, faster than 96.43% of C++ online submissions for All O`one Data Structure.
// Also super readable

/*
To break it down, two operations:
(1) cases when a new node is needed to be created in the list
(2) cases when a transfer (from a node to an adjacent node) is sufficient
Either is handled by a separate function
*/

#define um unordered_map

struct Node {
    int count;
    unordered_set <string> keys;
    Node (int count) {
        this->count = count;
    }
};


class AllOne {
public:
    um <string, list<Node>::iterator> store;
    list <Node> order;
    
    AllOne() {
        
    }
    
    void inc(string key) {
        if (store.find(key) == store.end()) {
            auto itr = order.begin();
            if (itr == order.end() || itr->count > 1) {
                // create new node and insert front
                Node * newnode = create_new_node(1, key);
                order.push_front(*newnode);
                store[key] = order.begin();
            } else {
                itr->keys.insert(key);
                store[key] = itr;
            }
        } else {
            auto itr = store[key];
            auto nextptr = next(itr);
            if (nextptr == order.end() || nextptr->count != itr->count + 1) {
                Node * newnode = create_new_node(itr->count + 1, key);
                // list.insert = insert before the iterator position
                auto pos = order.insert(nextptr, *newnode); 
                transfer_key(itr, pos, key);
            } else {
                // transfer key
                transfer_key(itr, nextptr, key);
            }
        }
    }
    
    void dec(string key) {
        /*
        workflow: 
        create node when: current count will be min of the list;
        previous count < current count - 1
        transfer key: else situation of the aforementioned
        */
        auto itr = store[key];
        auto prevptr = prev(itr);
        // situation that a new node is needed
        // or remove from data structure if count is 0
        if (itr == order.begin() || prevptr->count != itr->count - 1) {
            if (itr->count - 1 > 0) {
                Node * newnode = create_new_node(itr->count - 1, key);
                auto newptr = order.insert(itr, * newnode);
                itr->keys.erase(key);
                if (itr->keys.empty()) {
                    order.erase(itr);
                }
                store[key] = newptr;
            } else {
                itr->keys.erase(key);
                if (itr->keys.empty()) {
                    order.erase(itr);
                }
                store.erase(key);
            }
        } else {
            // situation that key can be transferred to the previous node
            transfer_key(itr, prevptr, key);
        }
    }

    Node * create_new_node(int count, string & key) {
        Node * newnode = new Node(count);
        newnode->keys.insert(key);
        return newnode;
    }

    void transfer_key(list <Node>::iterator & from, list <Node>::iterator & to, string & key) {
        to->keys.insert(key);
        from->keys.erase(key);
        if (from->keys.empty()) {
            order.erase(from);
        }
        store[key] = to;
    }
    
    string getMaxKey() {
        return order.empty() ? "" : *(order.back().keys.begin());
    }
    
    string getMinKey() {
        return order.empty() ? "" : *(order.front().keys.begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */