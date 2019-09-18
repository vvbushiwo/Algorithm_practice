"""
题目描述：
假设使用栈A与栈B模拟队列的功能
A为插入栈、B为弹出栈，以实现队列Q
假设A、B为空，可以认为栈A提供入队列的功能，栈B提供出队列的功能
入队列，入栈A即可，而出队列分二种情况
1、栈B不为空，则直接弹出栈B的数据
2、栈B为空，则依次弹出栈A的数据，放入栈B中，再弹出栈B的数据
"""
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0 :
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    def push(self, item):
        self.items.append(item)


class MyStack:
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.empty():
            while not self.A.empty():
                self.B.push(self.A.peek())
                self.A.pop()
        first = self.B.peek()
        self.B.pop()
        return first


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(3)
    print("队列的首元素为" + str(stack.pop()))
    print("队列的首元素为" + str(stack.pop()))


