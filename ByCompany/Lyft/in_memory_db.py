"""
Variation 1: in memory db

laptop coding 要做一个 in memory DB，要能 PUT / GET / DELETE / COUNTS_VAL (回传有几个值等于 val 的 keys)
然后还要能做 transaction block (begin / commit / rollback)
transaction 要能 nested，也就是可以 begin > begin > begin > rollback > commit etc.
Rollback 只会 rollback 最内层的那个 transaction，但 commit 会一次 commit 所有的


Example:
 SET a 1  
 BEGIN  
 GET a  # ===> (value = 1) 
 SET a 2  
 BEGIN 
 SET a 3 
 GET a # ====> (value = 3)  
 ROLLBACK  
 GET a # ====> (value = 2)  
 BEGIN  
 SET a 5 
 SET b 1  
 COMMIT  --> this will commit all the tx?
 GET a # ====> (value = 5) 
 GET b # ====> (value = 1)  

Adding UNSET
 SET a 1  
 BEGIN  
 UNSET a 
 GET a ===> NULL  
 ROLLBACK  
 GET a ===> 1  

Variation 2: in memory db with version number?

Variation 3: coinbase code signal coding
"""

from collections import deque
import sys

class Database:
    def __init__(self):
        self.db = dict()
        # implement transaction using stack
        """
        BEGIN: put {} on the stack 
        COMMIT: pop all from stack 
        ROLLBACK: pop last one from stack
        SET --> check if there is an open tx, 
        """
        self.tx = deque()

    def set(self, key, value):
        if not self.tx:
            self.db[key] = value
        else:
            current = self.tx[-1]
            current[key] = value
        
    def get(self, key):
        if not self.tx:
            if key not in self.db:
                return None
            return self.db[key]
        else:
            current = self.tx[-1]
            if key not in current:
                return None
            return current[key]
    
    def count_val(self, target):
        count = 0
        for _, v in self.db.items():
            if v == target:
                count += 1
        return count

    def begin(self):
        self.tx.append({})
    
    def rollback(self):
        self.tx.pop()
    
    """
    需要问清楚 是commit最后begin的那个transaction 还是commit 所有
    """
    def commit(self):
        while self.tx:
            commit = self.tx.popleft()
            for k, v in commit.items():
                if v is None:
                    # it is an unset tx 
                    if k not in self.db:
                        continue
                    else:
                        self.db[k] = None
                self.db[k] = v
        assert(len(self.tx) == 0)
    
    def delete(self):
        pass

    def unset(self, key):
        """
        how to commit an unset?
        """
        if not self.tx:
            if key not in self.db:
                return 
            self.db[key] = None
        else:
            current = self.tx[-1]
            current[key] = None


if __name__ == '__main__':
    db = Database()
    content = sys.stdin.read()
    lines = content.splitlines()
    for line in lines:
        line = line.split()
        if line[0] == 'SET':
            key, value = line[1], line[2]
            db.set(key, value)
        elif line[0] == 'GET':
            key = line[1]
            print(db.get(key))
        elif line[0] == 'ROLLBACK':
            db.rollback()
        elif line[0] == 'COMMIT':
            db.commit()
        elif line[0] == 'BEGIN':
            db.begin()