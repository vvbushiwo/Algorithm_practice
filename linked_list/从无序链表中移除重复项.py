class LNode:
    def _new_(self,x):
        self.data = x
        self.next = None
#带头节点的去除重复节点
def recursion_remove(head):
    if head.next is None:
            return  head
    else :
        pre = head
    #首先赋值二个指针
        head.next = recursion_remove(head.next)
        cur = head.next

        while cur  is not None:        #d当前的移动指针
            if head.data == cur.data:
                pre.next = cur.next
                cur   =    pre.next
            else:
                pre = pre.next
                cur = cur.next
    return head
def removeDup(head):
    if head is None:
        return
    head.next = recursion_remove(head.next)



if __name__ == "__main__":

    head = LNode()
    head.next = None
    head.data = None
    cur = head
    i = 1
    while(i <= 6):
        tmp = LNode()

        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i -2
        else:
            tmp.data= i

        tmp.next = None
        cur.next = tmp
        cur  = cur.next   #(指针后移)
        i += 1

    cur = head.next
    print("删除前")
    while cur is not None:
        print(cur.data)
        cur = cur.next
    recursion_remove(head)
    cur = head.next
    print("删除后")
    while cur is not None:
        print(cur.data)
        cur = cur.next