class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None



"""""""""""
题目要求：二个单链表加和
方法：链表对应位置相加，注意要有进位



"""""""""""


def add_linkedlist(head1, head2):

    # 考虑边界条件
    if head1 is None or head1.next is None:
        return head1

    if head2 is None or head2.next is None:
        return head2

    c = 0  # 考虑进位，赋值
    sum = 0  # 记录二个节点相加的值
    tmp = None  # 用来指向新创建的链表，加和链表的一个节点
    result = LNode()  # 新创建的链表节点
    result.next = None
    p = result  # 用来指向新链表的最后一个节点，即新链表移动的当前节点
    cur1 =head1.next
    cur2 = head2.next
    while cur1 is not None and cur2 is not None:
        tmp = LNode()
        tmp.next = None
        sum = cur1.data + cur2.data + c
        tmp.data = sum%10  #
        c = int(sum/10)
        p.next = tmp  # 移动指针
        p = tmp
        cur1 = cur1.next
        cur2 = cur2.next
    # 链表head2 比链表head1长 接下来只需要考虑head2剩余结点的值
    if cur1 is None:
        while cur2 is not None:
            tmp = LNode()
            tmp.next = None
            sum = head2.data + c
            tmp.data = sum % 10
            c = sum / 10
            p.next = tmp
            p = tmp
            cur2 = cur2.next

    if cur2 is None:
        while cur1 is not None:
            tmp = LNode()
            tmp.next = None
            sum = head1.data + c
            tmp.data = sum % 10
            c = sum / 10
            p.next = tmp
            p = tmp
            cur1 = cur1.next

    # 如何处理进位,计算后的进位
    if c == 1:
        tmp = LNode()
        tmp.next = None
        tmp.data = 1
        p.next = tmp
    return result
if __name__ == "__main__":
    i = 1
    head1 = LNode()
    head1.next = None
    head1.data = None
    cur1 = head1
    head2 = LNode()
    head2.next = None
    head2.data = None

    cur1 = head1
    cur2 = head2
    while i < 7:

        tmp = LNode()
        tmp.next = None
        if i < 4:
            tmp.data = i
            cur1.next = tmp
            cur1 = tmp  #让cur指针向后移动，不会一直覆盖头节点的值


        else:
            tmp.data = i + 3
            cur2.next = tmp
            cur2 = tmp


        i += 1
    print("显示数字：")
    cur1 = head1.next
    while cur1 is not None:
        print(cur1.data)
        cur1 = cur1.next
    print("显示数字：")
    cur2 = head2.next
    while cur2 is not None:
            print(cur2.data)
            cur2 = cur2.next
    print("相加后的结果：")
    head = add_linkedlist(head1,head2)
    cur  = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next









































