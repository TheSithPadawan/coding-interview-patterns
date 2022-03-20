/*
lc link: https://leetcode.com/problems/design-circular-queue/

In cpp just use STL list
*/
class MyCircularQueue {
public:
    int cap_;
    list <int> q;
    MyCircularQueue(int k) {
        cap_ = k;
    }
    
    bool enQueue(int value) {
        if (q.size() + 1 <= cap_) {
            q.push_back(value);
            return true;
        }
        return false;
    }
    
    bool deQueue() {
        if (q.size() == 0) return false;
        q.pop_front();
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return q.front();
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return q.back();
    }
    
    bool isEmpty() {
        return q.empty();
    }
    
    bool isFull() {
        return q.size() == cap_;
    }
};