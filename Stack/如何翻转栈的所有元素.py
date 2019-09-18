"""
题目描述：
翻转栈的所有元素，例如输入栈{1、2、3、4、5}，1在栈顶
翻转之后的栈为{5、4、3、2、1}，5在栈顶
思路：
递归调用
递归定义：
将当前的栈的最低元素移动到栈顶，其它元素顺次下移一位
然后对不包含栈顶元素的子栈进行同样操作
终止条件：
递归下去，栈为空
"""


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) is 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()  # 数组自带的函数list.pop()
        else:
            print("栈已经为空")
            return None

    # 压栈
    def push(self, item):
        self.items.append(item)

"""
方法功能：
把栈底的元素移动到栈顶
参数：栈的引用
"""


def move_bottom_to_top(s):
    if s.empty():
        return None
    top1 = s.peek()
    s.pop()  # 弹出栈顶元素
    if not s.empty():
        move_bottom_to_top(s)
        top2 = s.peek()
        s.pop()
        # 交换栈顶元素与子栈栈顶元素
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)


def reverse_stack(s):
    if s.empty():
        return
    move_bottom_to_top(s)
    top = s.peek()
    s.pop()
    reverse_stack(s)
    s.push(top)


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    reverse_stack(s)
    print("出栈顺序：")
    while not s.empty():
        print(s.peek())
        s.pop()
