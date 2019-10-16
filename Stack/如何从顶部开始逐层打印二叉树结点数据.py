"""
题目描述：给定一棵二叉树，要求逐层打印二叉树结点的数据
思路：
为了实现对二叉树的遍历，要求在遍历一个结点的同时，记录下它的孩子结点的信息，然后按照这个记录的顺序来访问结点的数据，在实现的时候可以采队列来存储当前遍历到的结点的孩子结点
"""
from collections import deque


class BitNode:
    def __init__(self):
        self.data = None
        self.l_child = None
        self.r_child = None


# 方法功能 把有序数组转换为二叉树
def array_to_tree(arr, start, end):
    root = None
    if end >= start:
        root = BitNode()
        mid = int((start + end + 1)/2)
        # 树的根节点为数组中间的元素
        root.data = arr[mid]
        # 递归的用左半部分数组构造root的左子树
        root.l_child = array_to_tree(arr, start, mid - 1)
        # 递归的用右半部分数组构造root的右子树
        root.r_child = array_to_tree(arr, mid + 1, end)
    else:
        root = None
    return root


"""
方法功能：用层序遍历的方式打印出二叉树结点的内容
输入参数：root二叉树根结点
"""


def print_layer_tree(root):
    if root == None:
        return
    queue = deque()
    # 树的根结点进队列
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        # 访问当前结点
        print(p.data)
        # 如果这个结点的左孩子不为空则入队列
        if p.l_child is not None:
            queue.append(p.l_child)
        # 如果这个结点的右孩子不为空则入队列
        if p.r_child is not None:
            queue.append(p.r_child)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = array_to_tree(arr, 0, len(arr) - 1)
    print("树的层序遍历结果为：")
    print_layer_tree(root)
