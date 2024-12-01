# https://leetcode.com/company/affirm/discuss/1530392/Affirm-or-Phone-or-find-POPUP

class Node:
    def __init__(self, id, hidden=False):
        self.is_hidden = hidden
        self.children = []
        self.id = id

    def add_children(self, nodes):
        self.children = nodes

# more optimized version 
def mark_nodes(node, parent):
    for c in node.children:
        if c.id != 'POPUP':
            c.is_hidden = True
    if parent:
        for c in parent.children:
            if c.id != node.id:
                c.is_hidden = True
"""
in dfs code 
for c in node.children:
    if c.val == 'POPUP':
        mark_nodes(node, parent)
        return

Initially put (root, None) as input value
"""
    
def find_pop_up(root: Node):
    pop_up_parent = None
    def dfs(node):
        nonlocal pop_up_parent
        if not node:
            return
        
        found = False
        for child in node.children:
            # found
            if child.id == 'POPUP':
                found = True
                print('Found POP UP Node')
                pop_up_parent = node
        # hide all children 
        if found:
            for child in node.children:
                child.is_hidden  = True
                print('Set Node', child.id, 'hidden to True')
            return
        if not found:
            for child in node.children:
                dfs(child)
    def hide_parent(node):
        if not node:
            return
        found = False
        for child in node.children:
            if child.id == pop_up_parent.id:
                found = True
        if found:
            for child in node.children:
                child.is_hidden = True
        else:
            for child in node.children:
                hide_parent(child)
    # step 1, find pop up and hide children
    dfs(root)
    # step 2, hide parent
    if pop_up_parent:
        print('here')
        hide_parent(root)


if __name__ == '__main__':
    root = Node("ROOT")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    root.add_children([B, C, D])

    F = Node("F")
    G = Node("G")
    POPUP = Node("POPUP", True)

    B.add_children([F, G])
    I = Node("I")
    J = Node("J")
    K = Node("K", True)

    D.add_children([POPUP, I, J, K])

    N = Node("N")
    O = Node("O")
    P = Node("P", True)

    POPUP.add_children([N, O, P])

    find_pop_up(root)
    # check child siblings
    print('is Node I hidden', I.is_hidden)
    print('is Node J hidden', J.is_hidden)

    # check parent sibling
    print('is Node B hidden', B.is_hidden)
    print('is Node C hidden', C.is_hidden)
