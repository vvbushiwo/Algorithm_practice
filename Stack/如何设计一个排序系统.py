""""
题目描述：
设计一个排序系统，能让每个进入队伍的用户都能看到自己在队列所处的位置和变化
队伍可能随时有人进、有人出、当有人退出影响用户的位置排名时，需要及时反馈到用户
思路：
1、实现队列的功能
2、随时可以退出队列，出队列之后，更新队列用户位置的变化
"""
from collections import deque


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_seq(self):
        return self.seq  # 当前的排队位置

    def set_seq(self, seq):
        self.seq = seq

    def get_id(self):
        return self.id

    def equals(self, arg0):
        o = arg0
        return self.id == o.get_id()
    # 这段话的含义是什么？

    def to_string(self):
        return "id:" + str(self.id) + " name:" + self.name + " seq:" + str(self.seq)


class MyQueue:
    def __init__(self):
        self.q = deque()

    def en_queue(self, u):  # 进入队列尾部
        u.set_seq(len(self.q) + 1)
        self.q.append(u)

    def de_queue(self):  # 队头出队列
        self.q.popleft()
        self.update_seq()

    def de_queue_move(self, u):
        self.q.remove(u)
        self.update_seq()

    def update_seq(self):
        i = 1
        for u in self.q:
            u.set_seq(i)
            i += 1

    # 打印队列的信息
    def print_list(self):
        for u in self.q:
            print(u.to_string())


if __name__=="__main__":
    u1 = User(1, "user1")
    u2 = User(2, "user2")
    u3 = User(3, "user3")
    u4 = User(4, "user4")
    queue = MyQueue()
    queue.en_queue(u1)
    queue.en_queue(u2)
    queue.en_queue(u3)
    queue.en_queue(u4)
    queue.de_queue()   # u1出队列
    queue.de_queue_move(u3)
    queue.print_list()