# https://www.1point3acres.com/bbs/thread-877599-1-1.html
"""
tl;dr - 1. Implement methods to grow a decision tree incrementally.
2. Use these methods to construct a given decision tree.
3. Evaluate this decision tree over multiple sets of signals.
 If the signal value is less than the constant we proceed down the left subtree and 
 if it is greater than or equal to the constant we proceed down the right subtree. 

 //            X1 < 3 <---- interior node (signal: "x1", constant: 3)
//         ------------
//        |            |
//     X2 < 1       X1 < 6
//  -----------    ---------
// |           |  |         |
// N           Y  N      X3 < 2
//                     ----------
//                    |          |
//                    Y          N <--- leaf node (Y/N)

// {X1: 2, X3: 1, X2: 11} -> Y

"""
class DecisionTreeNode:
    def __init__(self, signal_name=None, const=None) -> None:
        self.signal_name = signal_name
        self.constant = const
        self.left = None
        self.right = None
        self.value = 'Y'
    
    def eval(self, signals):
        if self.signal_name not in signals:
            print('Error in Decision Tree Signal')
            return
        print('evaluating node', self.signal_name, self.constant)
        if signals[self.signal_name] < self.constant:
            return self.left
        return self.right
    
    def get_leaf_result(self):
        return self.value

class DecisionTree:
    def __init__(self) -> None:
        self.root = DecisionTreeNode()

    def add_split(self, leaf: DecisionTreeNode, signal_name, constant):
        #     Add a split condition to the given leaf node.
        #   Return the newly created leaves for future calls.
        if not leaf:
            leaf = DecisionTreeNode()
        leaf.signal_name = signal_name
        leaf.constant = constant
        return leaf

    def set_leaf_value(self, leaf: DecisionTreeNode, value):
        leaf.value = value

    def evaluate(self, signals):
        """
        Evaluate the tree on a mapping of signal_name -> signal_value.
        Return the value of the leaf node reached by traversing the tree.
        """
        node = self.root
        while True:
            node = node.eval(signals)
            if not node.signal_name:
                break
        return node.get_leaf_result()


if __name__ == '__main__':
    tree = DecisionTree()
    tree.root = tree.add_split(tree.root, 'x1', 3)
    node1 = tree.add_split(tree.root.left, 'x2', 1)
    tree.root.left = node1
    node1_left = tree.add_split(node1.left, None, None)
    tree.set_leaf_value(node1_left, 'N')
    node1_right = tree.add_split(node1.right, None, None)
    node1.left = node1_left
    node1.right = node1_right

    tree.set_leaf_value(node1_right, 'Y')
    node2 = tree.add_split(tree.root.right, 'x1', 6)
    tree.root.right = node2
    node2_left = tree.add_split(node2, None, None)
    tree.set_leaf_value(node2_left, 'N')
    node2.left = node2_left
    node3 = tree.add_split(node2.right, 'x3', 2)
    node2.right = node3
    node3_left = tree.add_split(node3.left, None, None)
    tree.set_leaf_value(node3_left, 'Y')
    node3.left = node3_left
    node3_right = tree.add_split(node3.right, None, None)
    node3_left.right = node3
    tree.set_leaf_value(node3_right, 'N')
    print(tree.root.left)

    signals = {'x1': 2, 'x3': 1, 'x2': 11}
    print('---Evaluating Signals', signals, '---')
    print(tree.evaluate(signals))