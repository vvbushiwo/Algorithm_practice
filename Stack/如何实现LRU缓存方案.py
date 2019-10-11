"""
题目描述：LRU是指Least Recently Used 的缩写，它的意思是“最近最少使用”，LRU缓存就是使用这种原理。
即缓存一定量的数据，当超过设定的阈值，就把一些过期的数据删除掉
思路分析：
需要二个数据结构实现一个LRU缓存
1、使用双向链表实现的队列，队列最大容量为缓存的大小，使用过程中，把最近使用的页面移动到队列头，最近没有使用的页面放到队列尾
2、使用一个哈希表，把页号作为键，把缓存在队列中的结点的地址作为值。
当引用一个页面时，如果页面在内存中，只需要把这个页对应的结点移动到队列的前面。
如果所需的页面不在内存中，需要把这个页面加载到内存中
"""
from collections import deque


class LRU:
    def __init__(self, cachesize):
        self.cacheSize = cachesize
        self.queue = deque()
        self.hashSet = set()

    # 判断内存是否已满
    def is_queue_full(self):
        return len(self.queue) == self.cacheSize

    # 把页号为pageNum的页缓存到队列中，同时也添加到Hash表中
    def enqueue(self, page_num):
        # 如果队列已满，需要删除队尾的缓存页
        if self.is_queue_full():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(page_num)
        # 把新缓存的结点同时添加到hash表中
        self.hashSet.add(page_num)

    """ 
    当访问某一个page时，会调用这个函数，对于访问的page有两种情况
    1、page在缓存队列中，把这个结点直接移动到队首
    2、page不在缓存队列中，把page缓存到队首
    """
    def access_page(self, page_num):
        # page不在缓存队列，把它缓存到队首
        if page_num not in self.hashSet:
            self.enqueue(page_num)
        # page已经在缓存队列中，移动到队首
        elif page_num != self.queue[0]:
            self.queue.remove(page_num)
            self.queue.appendleft(page_num)

    def print_queue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


if __name__=="__main__":
    # 设缓存为3
    lru = LRU(3)
    # 访问page
    lru.access_page(1)
    lru.access_page(2)
    lru.access_page(5)
    lru.access_page(1)
    lru.access_page(6)
    lru.access_page(7)
    lru.print_queue()