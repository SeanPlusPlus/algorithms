class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def main():
    s = Stack()
    msg = "hello world"
    for char in msg:
        s.push(char)

    msg = ""
    while not s.isEmpty():
        msg += s.pop()

    print msg 

if __name__ == '__main__':
    main()
