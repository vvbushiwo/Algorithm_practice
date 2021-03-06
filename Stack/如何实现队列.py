"""
题目描述：
实现一个队列的数据结构，具有入队列、出队列、查看队列的首尾元素、查看队列大小等功能
思路：
1、数组实现
2、链表实现
"""

"""
# 数组实现
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0  # 队列头
        self.rear = 0   # 队列尾

    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear

    # 返回队列的大小
    def size(self):
        return self.rear - self.front

    # 返回队列首元素
    def get_front(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    # 返回队列尾元素
    def get_rear(self):
        if self.is_empty():
            return None
        return self.arr[self.rear - 1]

    # 删除队列头元素
    def de_queue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列已经为空")

    # 把新元素加入队列尾
    def add_queue(self, item):
        self.arr.append(item)
        self.rear += 1

"""


class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


class MyQueue:
    # 分配头节点
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    # 判断队列是否为空，如果为空返回true，否则返回false
    def empty(self):
        if self.pHead is None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.pHead
        while p is not None:
            p = p.next
            size += 1
        return size

    # 入队列：把元素e加到队列尾
    def add_queue(self, e):
        p = LNode()
        p.data = e
        p.next = None
        if self.pHead is None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p

    # 出队列，删除队列的首元素
    def de_queue(self):
        if self.pHead is None:
            print("出队列失败，队列已经为空")
        self.pHead = self.pHead.next
        if self.pHead is None:
            self.pEnd is None

    # 取得队列首元素
    def get_front(self):
        if self.pHead is None:
            print("获取队列首元素失败，队列已经为空")
            return None
        return self.pHead.data

    # 取得队列尾元素
    def get_rear(self):
        if self.pEnd is None:
            print("获取队列尾元素失败，队列为空")
            return None
        return self.pEnd.data


if __name__ == "__main__":
    queue = MyQueue()
    queue.add_queue(1)
    queue.add_queue(2)
    print("队列头元素为：" + str(queue.get_front()))
    print("队列尾元素：" + str(queue.get_rear()))
    print("队列大小" + str(queue.size()))

