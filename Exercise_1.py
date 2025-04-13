class Stack:
    """Simple stack implementation using a list"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()


def reverse_string(s):
    """Reverse a string using a stack"""
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    result = reverse_string(user_input)
    print("Reversed string:", result)
