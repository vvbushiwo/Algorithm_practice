"""
题目描述：
假设给定链表1-2-3-4-5-6-7中指向第5个元素的指针，要求把结点5删掉，删除后链表变为1-2-3-4-6-7
思路：
1、如果这个结点是链表的最后一个结点是无法删除的（题目条件）
2、如果这个结点不是最后一个结点，可以通过把其后继结点的数据复制到当前结点，
然后删除后继结点的方法来实现
"""


class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


# 构造链表
def construct_list(number):
    i = 1
    head = LNode()
    cur = head
    while i < number:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i +=1
    return head, p


# 打印链表
def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


def remove_node(p):
    # 如果结点为空，或者结点p无后继结点则无法删除
    if p is None or p.next is None:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True


if __name__ == "__main__":
    head, p = construct_list(8)
    print("删除结点前的链表")
    print_list(head)
    result = remove_node(p)
    if result is True:
        print("删除节点后的链表")
        print_list(head)
