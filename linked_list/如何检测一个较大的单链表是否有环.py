"""
题目描述：单链表有环，指的是
单链表中的某一个结点的next域指向的是链表中在它之前的某一个结点。
这样在链表的尾部形成一个环形结构，如何判断单链表是否有环存在？

分析：
采用双指针的方法，快指针会在环内循环，因此慢指针会与快指针相遇，即证明有环
slow指针进入环后，只要再走m步（fast落后slow指针的节点数）就一定会和fast指针相遇。
slow指针进入环后，假设fast指针再往前走m个节点就会到达当前slow指针的位置，
那么当slow指针和fast指针同时移动的时候，slow指针每向前移动一个节点，fast指针就会向前移动两个节点，
fast与slow之间的距离就会缩短一个，所以当移动m步之后，fast指针就会和slow指针相遇。

fast 走的长度=2s
slow 走的长度=s
2s = s + nr
s = nr
整个链表长度为L，入口环与相遇点距离为x，起点到环入口距离为a，
则满足如下关系表达式：
a+x = nr
a+x = (n-1)r +r = (n-1)r +L-a
a = (n-1)r+L-a-x
规律：
L-a-x 为相遇点到环入口的长度，
起点到环入口点的距离 = （n-1）*环长+ 相遇点到环入口的长度
于是从起点和相遇点设置指针，每次各走一步，二个指针必定相遇，
相遇点为环起点
"""


class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


# 构造链表
def cons_list(long):
    i = 1
    head = LNode()
    head.next = None
    cur = head
    while i < long:
        tmp = LNode()
        tmp.next = None
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = head.next.next.next.next.next   # 构建环
    return head


"""
判断链表是否有环
"""


def is_loop(head):
    if head is None or head.next is None:
        return None
    # 初始结点指向首结点
    slow = head.next
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


"""
function：
找出环的入口点
输入：head 链表头结点、相遇点
返回值：
None 代表无环
否则返回环的入口点
"""


def find_loop_node(head,meet_node):
    first = head.next
    while first is not None and first.next is not None:
        first = first.next
        meet_node = meet_node.next
        if first == meet_node:
            return first
    return None


if __name__=="__main__":
    head = cons_list(15)
    meet_node = is_loop(head)
    if meet_node is not None:
        print("有环")
        loop_node = find_loop_node(head,meet_node)
        print("环的入口点为：", str(loop_node.data))
    else:
        print('无环')
