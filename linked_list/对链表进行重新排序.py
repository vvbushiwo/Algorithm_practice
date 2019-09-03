class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


"""
题目要求：给定链表L0-L1-L2···-Ln1，把链表重新排序L0-Ln-L1-Ln-1-L2-Ln-2···
条件1：在原来的链表基础上排序，即不能申请新的结点
条件2：只能修改结点的next域，不能修改数据域。
方法：找出链表head的中间结点，把链表从中间断成两个子链表
输入参数：head链表结点
返回值：链表中间结点
"""


def FindMiddleNode(head):
    if head is None or head.next is None:
        return head
    fast = head  # 遍历链表的时候每次向前走两步
    slow = head  # 遍历链表的时候每次向前走一步
    slowPre = head
    # 当fast到链表尾时，slow恰好指向链表的中间结点
    while fast is not None and fast.next is not None:
        slowPre = slow
        slow = slow.next
        fast = fast.next.next
    slowPre.next = None
    return slow


# 函数功能，实现逆序
def Reverse(head):
    if head == None or head.next == None:
        return head
    pre = head
    cur = head.next
    pre.next = None
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur  # 前驱结点向后移动
        cur = next
    return pre


#

def Reorder(head):
    if head == None or head.next == None:
        return
    # 前半部分链表第一个结点
    cur1 = head.next
    mid = FindMiddleNode(head.next)  # 执行过后，head后面的内容，在内存中保存在同一位置，因此mid把链表后半部分截走后，cur1只有一半的链表

    # 后半部分的第一个结点
    cur2= Reverse(mid)

    # 合并二个链表
    while cur1 is not None:
        tmp = cur1.next   #把cur1后面的链表内容单独拿出来
        cur1.next = cur2 #其实是对有头结点的链表后面接上cur2的链表内容
        cur1 = tmp  # cur1 向后移动一位，占用新的空间
        if cur1 is not None:
            tmp = cur2.next
            cur2.next = cur1
            cur2 = tmp



    return cur1


if __name__ == "__main__":
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    #  构造第一个链表
    while i < 55:
        tmp = LNode()
        tmp.next = None
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i += 1
    print("排序前：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    Reorder(head)
    print("排序后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next

