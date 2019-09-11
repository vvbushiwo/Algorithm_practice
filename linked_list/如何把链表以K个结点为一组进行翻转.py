"""
题目描述：
K链表翻转是指把每k个相邻的结点看成一组进行翻转
如果剩余结点不足k个，则保持不变

例如：假设给定链表1-2-3-4-5-6-7和一个k，如果k
值为2，那么翻转后的链表为2-1-3-4-6-5-7
如果是k=3，那么翻转后的链表为3-2-1-6-5-4-7

思路：
把前k个结点看成一个子链表，用翻转子链表的做法
翻转后连上上一个翻转后的子链表
以k=3为例
1、首先设置pre指向头节点，然后让第一组的结点begin 指向链表第一个结点
找到从begin开始第k=3个的结点end，第一轮的指针
2、链表逆序，需要使得end.next =None 在此之前需要记录下end指向的结点，即pnext，为了之后接上来链表
3、end.next = None,从而使得从begin 到end为一个单链表
4、以begin为第一个结点，end为尾节点所对应的k=3个结点进行翻转
5、由于翻转后子链表的第一个结点从begin变为end，因此，执行pre.next = end,把翻转后的子链表连接起来
6、把链表中剩余的还未完成翻转的子链表连接到已经完成翻转的子链表后面
7、让pre指针指向已完成翻转的链表的最后一个结点
8、让begin指针指向下一个需要被翻转的子链表的第一个结点
剩余循环
"""


class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


# 对不带头节点的单链表逆序
def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    pre.next = None

    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

# 对链表k进行翻转


def reverse_k(head, k):
    if head is None or head.next is None or k < 2:
        return
    i = 1
    pre = head
    begin = head.next
    while begin is not None:  # 找到begin开始第k个结点
        end = begin
        while i < k:
            if end.next is not None:
                end = end.next
            else:              # 剩余结点的个数小于k
                return
            i += 1
        pNext = end.next   # 完成第2步
        end.next = None    # 第3步
        pre.next = reverse(begin)  # 完成逆序
        begin.next = pNext  # 完成逆序后连接链表
        pre = begin
        begin = pNext
        i = 1
    return head


def construct_list(number):
    i = 1
    a = number
    head = LNode()
    head.next = None

    cur = head
    while i < a:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1
    return head


if __name__=="__main__":
    head = construct_list(8)
    print("顺序输出")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    reverse_k(head, 3)
    print("逆序输出：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


