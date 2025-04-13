class TextEditor:
    def __init__(self):
        self.text_stack = []      
        self.undo_stack = []      

    def type(self, char):
        """Type a character."""
        self.text_stack.append(char)
        self.undo_stack.append(('type', char))

    def delete(self):
        """Delete the last character."""
        if self.text_stack:
            deleted_char = self.text_stack.pop()
            self.undo_stack.append(('delete', deleted_char))

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            return

        action, char = self.undo_stack.pop()
        if action == 'type':
            self.text_stack.pop()  
        elif action == 'delete':
            self.text_stack.append(char) 

    def get_text(self):
        """Return current text as a string."""
        return ''.join(self.text_stack)


if __name__ == "__main__":
    # Test Case 1
    print("Test Case 1:")
    editor = TextEditor()
    editor.type('H')
    editor.type('e')
    editor.type('l')
    editor.type('l')
    editor.type('o')
    print("Text after typing 'Hello':", editor.get_text())

    editor.delete()
    print("Text after deleting last character:", editor.get_text())

    editor.undo()
    print("Text after undoing delete:", editor.get_text())

    editor.undo()
    print("Text after undoing last type:", editor.get_text())
    print()

    # Test Case 2
    print("Test Case 2:")
    editor = TextEditor()
    for char in "Stack":
        editor.type(char)
    print("Text after typing 'Stack':", editor.get_text())

    editor.delete()
    print("Text after deleting last character:", editor.get_text())

    editor.undo()
    print("Text after undoing delete:", editor.get_text())

    editor.undo()
    print("Text after undoing last type:", editor.get_text())
    print()

    # Test Case 3
    print("Test Case 3:")
    editor = TextEditor()
    editor.type('A')
    editor.type('B')
    editor.type('C')
    print("Text after typing 'ABC':", editor.get_text())

    editor.undo()
    print("Text after undoing last type:", editor.get_text())

    editor.undo()
    print("Text after undoing last type:", editor.get_text())

    editor.undo()
    print("Text after undoing last type:", editor.get_text())
