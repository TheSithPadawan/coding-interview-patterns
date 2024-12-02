"""
In typical Object Oriented world,
a stack has two methods that mutate the data of the stack that is being operated on, push() and pop().
We'd like to implement an immutable version of the class, which we'll call PStack.
# Psuedocde class PStack
PStack() # constructor
int size() # returns number of elements in the stack
int peek() # returns the most recently pushed element
PStack push(int) # returns an instance of PStack with the element added
PStack pop() # returns an instance of Pstack with the top element removed
需要做到 Push 和 Pop 都是O（1）。Follow up 是实现 reverse()。
"""

class PStack:
    def __init__(self, head=None, tail=None) -> None:
        self.tail = tail
        self.head = head
        self.count = 0
    
    def push(self, val):
        st = PStack(head=val, tail=self)
        st.count = self.count + 1
        return st
    
    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None
    
    def pop(self):
        if not self.head:
            # do not allow popping an empty pstack
            print('Error: popping from an empty stack')
            return
        self.count -= 1
        return self.tail

    def peek(self):
        return self.head

    def reverse(self):
        reverse_stack = PStack()
        current = self
        while not current.is_empty():
            print(f'pushing {current.head} to reverse_stack')
            reverse_stack = reverse_stack.push(current.head)
            current = current.tail
        return reverse_stack
    
    def visualize_as_list(self):
        print('---visualizing stack---')
        result = []
        current = self
        while not current.is_empty():
            result.append(current.head)
            current = current.tail
        return result[::-1]


if __name__ == '__main__':
    # stack1 = []
    stack1 = PStack()
    # stack2 = [10]
    stack2 = stack1.push(10)
    print(stack2.visualize_as_list())
    # stack3 = [10, 20]
    stack3 = stack2.push(20)
    print(f'Stack 3 has {stack3.size()} elements')
    print(stack3.visualize_as_list())
    # stack4 = [10]
    stack4 = stack3.pop()
    print(f'Stack 4 has {stack4.size()} elements')
    print(f'top element of stack4 is {stack4.peek()}')
    print(stack4.visualize_as_list())
    # reverse stack 3
    stack5 = stack3.reverse()
    # stack 3 is still [10, 20]
    print(stack3.visualize_as_list())
    print(stack5.visualize_as_list())
