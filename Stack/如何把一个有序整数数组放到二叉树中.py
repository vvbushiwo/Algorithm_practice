"""
题目分析：
把有序数组放入二叉数，构造出来的二叉树也是一棵有序的二叉树
实现思路：
取数组中间的元素作为根结点，将数组分为左右二个部分
对数组的二部分用递归的方法分别构建左右子树
"""
import math

def arr1(n):
    i = 1
    arr_1 = []
    while i < n:
        arr_1.append(i)
        i += 1
    return arr_1


class BiTNode:
    def __init__(self):
        self.data = None
        self.l_child = None
        self.r_child = None


# 方法功能：把有序数组转换为二叉树
def array_to_tree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = int((start + end + 1)/2)
        # 树的根结点为数组中间的元素
        root.data = arr[mid]
        root.l_child = array_to_tree(arr, start, (mid - 1))
        # 递归的用右半部分数组构造root的右子树
        root.r_child = array_to_tree(arr, mid+1, end)
    else:
        root = None
    return root


# 用中序遍历的方法打印出二叉树结点的内容
def print_tree_mid_order(root):
    if root == None:
        return
    # 遍历root结点的左子树
    if root.l_child is not None:
        print_tree_mid_order(root.l_child)
    # 遍历root结点
    print(root.data)
    # 遍历root结点的右子树
    if root.r_child is not None:
        print_tree_mid_order(root.r_child)


if __name__ == "__main__":
    arr = arr1(12)
    print("数组：")
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1
    a = len(arr) - 1
    print("\n")
    root = array_to_tree(arr, 0, a)
    print("转换成树的中序遍历：")
    print_tree_mid_order(root)
