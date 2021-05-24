#implementation of a stack using lists
class My_stack:
    
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return size(self.stack) == 0

    def push(self, num):
        self.stack.insert(num, 0)
        len(self.stack) += 1

    def pop(self):
        if isEmpty(self.stack):
            print("stack is empty, can not pop any more")
        else:
            num = self.stack.pop(0)
            len(self.stack) -= 1
        return num


class My_queue:

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue) == 0
    def push(self, num):
        self.queue.append(num)
        len(self.stack) += 1

    def pop(self):
        if isEmpty(self.stack):
            print("queue is empty, can not pop any more")
        else:
            num = self.queue.pop(0)
            len(self.queue) -= 1
        return num
        
        
