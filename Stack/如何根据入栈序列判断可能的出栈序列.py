"""
题目描述：
输入二个整数序列，其中一个序列表示栈的push（入）顺序，判断另一个序列有没有
可能是对应的pop顺序
思路：
用一个栈来模拟入栈顺序，具体步骤如下：
1、把push序列依次入栈，直到栈顶元素等于pop序列的第一个元素
然后栈顶元素出栈，pop序列移动到第二个元素
2、如果栈顶继续等于pop序列现在的元素，则继续出栈并pop后移
否则对push序列继续入栈
3、如果push序列已经全部入栈，但pop序列未完全遍历，而且栈顶元素
不等于当前pop元素，那么这个序列不是一个可能的出栈序列。
如果栈为空，而且pop序列也全部被遍历，则说明这是一个可能的pop序列
"""


class Stack:
    def __init__(self):
        self.items = []
    # 判断栈是否为空

    def empty(self):
        return len(self.items) == 0

    # 返回栈的大小
    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[(len(self.items) - 1)]
        else:
            return None

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")

    # 压栈
    def push(self, item):
        self.items.append(item)


def is_pop_serial(push, pop):
    if push is None or pop is None:
        return False
    push_len = len(push)
    pop_len = len(pop)
    if push_len is not pop_len:
        return False
    push_index = 0
    pop_index = 0
    stack = Stack()
    while push_index < push_len:
        # 把push序列依次入栈，直到栈顶元素等于pop序列的第一个元素
        stack.push(push[push_index])
        push_index += 1
        # 栈顶元素出栈，pop序列移动到下个元素
        while (not stack.empty()) and stack.peek() == pop[pop_index]:
            stack.pop()
            pop_index += 1
        # 栈为空，且pop序列中元素都被遍历过
    return stack.empty() and pop_index == pop_len


if __name__ == "__main__":
    push = "12345"
    pop = "53412"
    if is_pop_serial(push, pop):
        print(pop + "是" + push + "的一个pop序列")
    else:
        print(pop+"不是"+push+"的一个pop序列")

