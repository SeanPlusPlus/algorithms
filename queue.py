class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

def main():
    q = Queue()

    li = ['a', 'b', 'c', 'd']
    for el in li:
        q.enqueue(el)

    while not q.isEmpty():
        print q.dequeue()

if __name__ == '__main__':
    main()
