"""
题目描述：
单链表交叉是指二个链表存在完全重合的部分
且找出交叉的部分
思路：
尾节点法
如果二个链表相交，那么从相交点到尾节点都是相同节点
所以判断二个链表的最后一个节点是不是相同即可
1、先遍历一个链表，直到尾部
2、再遍历另一个链表，如果也能走到同样的尾节点，则二个链表相交
记下二个链表的长度n1、n2
3、再遍历一次，长链表节点先出发前进|n1-n2|
4、之后同时前进，每次一步，相遇的第一点即为相交第一个点
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
        if i == 4:
            p = tmp
        i +=1
    return head, p


def construct_list_y(number):
    i = 1
    head1, p = construct_list(8)
    head2 = LNode()
    cur = head2
    tmp = LNode()
    while i < number:
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = p
    return head1, head2


# 打印链表
def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next

# 判断二个链表是否相交，如果相交找出交点
# 输入参数：head1、head2分别为二个链表的头节点
# 返回值：如果不相交返回None，如果相交返回相交节点


def is_intersect(head1, head2):
    if head1 is None or head1.next is None or head2 is None or head2.next is None or head1 == head2:
        return None
    temp1 = head1.next
    temp2 = head2.next
    n1, n2 =0, 0
    # 遍历head1，找到尾节点，同时记录head1的长度
    while temp1.next is not None:
        temp1 = temp1.next
        n1 += 1
    # 遍历head2，找到尾节点，同时记录head2的长度
    while temp2.next is not None:
        temp2 = temp2.next
        n2 += 1
    if temp1 == temp2:
        # 长链表先走|n1-n2|步
        if n1 > n2:
            while n1-n2 > 0:
                head1 = head1.next
                n1 -= 1
        if n2 > n1:
            while n2-n1 > 0:
                head2 = head2.next
                n2 -= 1
        # 二个链表同时前进，找到相同的节点
        while head1 is not head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None


if __name__ == "__main__":
    head1, head2 = construct_list_y(2)
    print("链表1")
    print_list(head1)
    print("链表2")
    print_list(head2)
    meet_node = is_intersect(head1, head2)
    if meet_node is None:
        print("链表不相交")
    else:
        print("链表相交的交点为："+str(meet_node.data))
