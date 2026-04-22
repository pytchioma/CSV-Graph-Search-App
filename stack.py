# =========================
# STACK CLASS
# =========================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# =========================
# 1. REVERSE STRING
# =========================

def reverse_string(text):
    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text


# =========================
# 2. CHECK BALANCED PARENTHESES
# =========================

def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


# =========================
# 3. UNDO SYSTEM
# =========================

def simulate_undo(actions):
    stack = Stack()

    for action in actions:
        if action == "UNDO":
            if not stack.is_empty():
                stack.pop()
        else:
            stack.push(action)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    return result[::-1]


# =========================
# TESTING EVERYTHING
# =========================

if __name__ == "__main__":

    print("=== Reverse String ===")
    print(reverse_string("hello"))  # olleh
    print(reverse_string("Chioma")) # amoihC

    print("\n=== Balanced Parentheses ===")
    print(is_balanced("(a + b)"))      # True
    print(is_balanced("(a + b]"))      # False
    print(is_balanced("((a + b))"))    # True
    print(is_balanced("([)]"))         # False

    print("\n=== Undo System ===")
    actions = ["type A", "type B", "UNDO", "type C"]
    print(simulate_undo(actions))  # ['type A', 'type C']

    # =========================
# NODE CLASS
# =========================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# =========================
# STACK (LINKED LIST VERSION)
# =========================

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        removed_value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return removed_value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count
    
    # =========================
# PART 4 — SHORT ANSWERS
# =========================

# 1. Why are push and pop O(1) in a stack?
# Because they only operate on the top element.
# No matter how many items are in the stack,
# push adds one item and pop removes one item directly,
# without looping through the structure.

# 2. What makes a stack different from a queue?
# A stack uses LIFO (Last In, First Out) — last item added is removed first.
# A queue uses FIFO (First In, First Out) — first item added is removed first.

# 3. Name two real-world systems that use stack behavior.
# - Undo/redo systems in text editors
# - Browser history (back button)