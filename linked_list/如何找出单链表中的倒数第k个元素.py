'''
题目描述：找出单链表中的倒数第k个元素，例如给定单链表：1->2->3->4->5->6->7
则单链表的倒数第k=3的元素为5
方法为快慢指针法，从头到尾进行遍历查找，在查找过程中，设置二个指针，让其中的一个指针比另一个指针先移动k步，
然后二个指针同时向前移动，循环直到先行指针为None时，另一个指针所指就是需要的值
'''

class LNode():
    def _new_(self,x):
        self.data = x
        self.next = None
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
#打印链表
def print_List(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
"""
方法功能：找出链表倒数的K个结点
输入参数：head 链表头节点
返回值：倒数的k个结点
"""
def Find_Last_k(head,k):
    if head is None or head.next is None:
        return head
    #初始化结点定义
    slow = LNode()
    fast = LNode()
    slow = head.next
    fast = head.next

    i = 0
    while i <k and fast is not None:
        fast = fast.next #向前移动K步
        i += 1
    if i < k :
        return None
    while fast != None:
        slow  = slow.next
        fast = fast.next
    return slow
if __name__== "__main__":
    head = ConstructList(8)
    print("链表:")
    print_List(head)
    result = Find_Last_k(head,3)
    if result is not None:
        print("\n 链表倒数第三个链表的元素为："+str(result.data))


