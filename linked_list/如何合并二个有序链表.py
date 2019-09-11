"""
题目描述：
已知二个链表各自有序，head1、head2
请合并，合并后有序
思路：
分别用指针head1、head2来遍历二个链表，当前head1指向的数据小于head2指向的数据，则将head1指向的结点归入合并后链表中
否则，将head2指向的结点归入合并后的链表，
当有一个链表遍历结束，则把未结束的链表连接到合并后的链表尾部
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
        tmp.data = i*2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1
    return head


# 打印链表
def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


# 合并链表
def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    head = None # 合并后的结点
    cur = None
    # 合并后链表的头节点为第一个结点元素最小的那个链表的头节点
    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next
    # 每次找链表剩余结点的最小值对应的结点连接到合并后链表的尾部
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    # 当遍历完一个链表后把另外一个链表剩余的结点连接到合并后链表后面
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head


if __name__ == "__main__":
    head1 = construct_list(8)
    head2 = construct_list(6)
    print("链表1\n")
    print_list(head1)
    print("链表2\n")
    print_list(head2)
    print("合并后的链表：\n")
    head = merge(head1, head2)
    print_list(head)
