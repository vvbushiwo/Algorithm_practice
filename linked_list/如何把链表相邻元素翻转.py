"""
题目描述：
把链表相邻元素翻转，，例如给出1-2-3-4-5-6-7，则翻转链表后，变为2-1-4-3-6-5-7
方法：
就地逆序
思路：调整结点指针域的指向来直接交换相邻的两个结点。如果单链表恰好有偶数个结点，那么只需要将奇偶结点对调即可
如果单链表有奇数个，那么只需要将最后一个结点之前的结点对调即可。
逆序6步：
先定义指针
pre前驱指针 cur当前指针 next后继指针
1、将当前指针的next指针后移动一位，为的是逆序后不丢失链表后面的内容
2、pre指针指向cur.next 完成后项结点变前项结点
3、当后项结点变为前项结点，需要指向之前的前项结点，完成交换
4、此时已经完成交换，需要交换后的链表接上后续内容，即cur.next = next
5、pre指针向后移动2位
6、cur指针向后移动2位，重复上述4步，完成整个链表的相邻元素翻转
"""


class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return
    pre = head
    cur = head.next
    while cur is not None and cur.next is not None:
         next = cur.next.next  # 第一步
         pre.next = cur.next  # 第二步
         cur.next.next = cur  # 第三步
         cur.next  = next  # 第四步
         pre = cur         # 第五步
         cur = next        # 第六步
    return head

#构造一个单链表
def   ConstructList(number):
    i = 1
    a = number
    head = LNode()
    head.next = None

    cur = head
    while  i < a:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1
    return head


if __name__ == "__main__":
    head = ConstructList(9)
    print("\n 逆序前：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    print("\n 逆序后：")
    head = reverse(head)
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
