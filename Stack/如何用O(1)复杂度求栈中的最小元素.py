"""
题目描述：
用O(1)的时间复杂度求栈中最小的元素
思路：
空间换时间
用二个栈结构，一个栈用来存储数据
另外一个用来存储栈的最小元素
当前入栈元素比原来栈的最小值还小，则把这个值压入保存的最小元素的栈中
在出栈的时候，如果当前出栈的元素恰好为当前栈的最小值，保存最小值的栈顶元素也出栈
设定当前最小值变为当前最小值入栈前的最小值
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
            return self.items[len(self.items) - 1 ]

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    def push(self, items):
        self.items.append(items)


class MyStack:
    def __init__(self):
        self.elemStack = Stack()  # 用来存储栈中元素
        self.minStack = Stack()  # 栈顶永远存储当前elemStack 中最小的值

    def push(self, data):
        self.elemStack.push(data)
        # 更新保存最小元素的栈
        if self.minStack.empty():
            self.minStack.push(data)
        else:
            if data < self.minStack.peek():
                self.minStack.push(data)

    def pop(self):
        top_data = self.elemStack.peek()
        self.elemStack.pop()
        if top_data == self.mins():
            self.minStack.pop()
        return top_data

    def mins(self):
        if self.minStack.empty():
            return False
        else:
            return self.minStack.peek()


if __name__ == "__main__":
    stack = MyStack()
    stack.push(5)
    print("栈中的元素最小值为" + str(stack.mins()))
    stack.push(6)
    print("栈中的最小元素的值为" + str(stack.mins()))
