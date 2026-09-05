class Stack:
    def __init__(self):
        self.new_list = []

    def is_empty(self):
        if len(self.new_list) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.new_list.append(item)

    def pop(self):
        return self.new_list.pop()

    def peek(self):
        return self.new_list[len(self.new_list) - 1]

    def size(self):
        return len(self.new_list)



def is_balanced(new_str):
    char_list = list(new_str)
    my_stack = Stack()
    for item in char_list:
        if item == '(' or item == '[' or item == '{':
            my_stack.push(item)
        elif item == ')' or item == ']' or item == '}':
            if my_stack.is_empty():
                return "Несбалансированно"
            if my_stack.peek() == '(' and item == ')' or my_stack.peek() == '[' and item == ']' or my_stack.peek() == '{' and item == '}':
                my_stack.pop()
            else:
                return "Несбалансированно"
    if my_stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

data = input("Введите строку: ")
print(is_balanced(data))