class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.main_stack:
            raise IndexError("Stack is empty")
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.main_stack:
            raise IndexError("Stack is empty")
        return self.main_stack[-1]

    def getMin(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]


if __name__ == "__main__":
    # Test Case 1
    print("Test Case 1:")
    stack1 = MinStack()
    stack1.push(5)
    stack1.push(3)
    stack1.push(7)
    stack1.push(2)

    print("Top element:", stack1.top())        
    print("Minimum:", stack1.getMin())          

    stack1.pop()
    print("Top element after pop:", stack1.top())     
    print("Minimum after pop:", stack1.getMin())      
    print("")

    # Test Case 2
    print("Test Case 2:")
    stack2 = MinStack()
    stack2.push(8)
    stack2.push(6)
    stack2.push(9)
    stack2.push(4)

    print("Top element:", stack2.top())        
    print("Minimum:", stack2.getMin())          

    stack2.pop()
    print("Top element after pop:", stack2.top())     
    print("Minimum after pop:", stack2.getMin())     
    print("")

    # Test Case 3
    print("Test Case 3:")
    stack3 = MinStack()
    stack3.push(10)
    stack3.push(1)
    stack3.push(3)
    stack3.push(2)

    print("Top element:", stack3.top())        
    print("Minimum:", stack3.getMin())        

    stack3.pop()
    print("Top element after pop:", stack3.top())    
    print("Minimum after pop:", stack3.getMin())     
