"""
题目描述：
给定一个有序链表，其中每一个节点也是一个有序链表，节点包含二个类型的指针
1、指向主链表中下一个节点的指针
2、指向此节点头的链表
所有链表都被排序

思路：
归并排序中的合并排序
递归的合并已经扁平化的链表与当前链表
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.down = None


class MergeList:
    def __init__(self):
        self.head = None

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return b
        if a.data < b.data:
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)
        return result

# 链表扁平化处理
    def flatten(self, root):
        if root is None or root.right is None:
            return root
    # 递归处理root.right链表
        root.right = self.flatten(root.right)
        root = self.merge(root, root.right)
        return root
# 把data插入链表头

    def insert(self, head_ref, data):
        new_node = Node(data)
        new_node.down = head_ref
        head_ref = new_node
        return head_ref

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.down


if __name__ == "__main__":
    L = MergeList()
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)

# 扁平化链表
    L.head = L.flatten(L.head)
    L.print_list()
