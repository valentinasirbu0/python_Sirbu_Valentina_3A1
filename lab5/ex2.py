class Queue:
    def __init__(self):
        self.vector = []

    def __str__(self):
        return f"Stack: {self.vector}"

    def push(self, elem):
        self.vector.append(elem)

    def pop(self):
        if len(self.vector) > 0:
            self.vector.pop(0)
        else:
            return None

    def peek(self):
        if len(self.vector) > 0:
            return self.vector[0]
        else:
            return None


s1 = Queue()
s1.push(3)
s1.push(4)
s1.push(5)
print(s1.peek())
s1.pop()
print(s1)
