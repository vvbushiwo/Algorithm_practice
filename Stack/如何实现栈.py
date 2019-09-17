"""
题目描述：
实现栈，具有压栈、弹栈、取栈顶元素
判断栈是否为空以及获取栈中元素个数
方法1：数组实现
方法2：链表实现
"""

"""
# 方法1
class MyStack:
    # 模拟栈
    def __init__(self):
        self.items = []
    # 判断栈是否为空

    def is_empty(self):
        return len(self.items) == 0

    # 返回栈的大小

    def size(self):
        return len(self.items)

    # 返回栈顶元素

    def top(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    # 压栈

    def push(self, item):
        self.items.append(item)
"""


# 方法2
class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    def empty(self):
        if self.next is None:
            return True
        else:
            return False
        # 获取栈中元素

    def size(self):
        size = 0
        p = self.next
        while p is not None:
            p = p.next
            size += 1
        return size
    # 入栈：把e放入栈顶

    def push(self, e):
        p = LNode()
        p.data = e
        p.next = self.next
        self.next = p

    # 出栈
    def pop(self):
        tmp = self.next
        if tmp is not None:
            self.next = tmp.next
            return tmp.data
        print("栈已经为空")
        return None

    # 取得栈顶元素
    def top(self):
        if self.next is not None:
            return self.next.data
        print("栈已经为空")
        return None


if __name__ == "__main__":
    s = MyStack()
    s.push(4)
    s.push(6)
    print("栈顶元素：" + str(s.top()))
    print("栈大小为：" + str(s.size()))
    s.pop()
    print("弹栈成功")
    s.pop()
    s.pop()
