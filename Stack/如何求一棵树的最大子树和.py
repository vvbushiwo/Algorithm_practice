"""
题目描述：
给定一棵二叉树，每个结点都是正整数或负整数，如何找到一棵子树，使得它所有结点和最大
思路分析：
针对每棵子树，求出所有结点和，如果遍历当前结点的值与其左右子树和的值相加的结果大于最大值，则更新最大值
"""


class BitNode:
    def __init__(self):
        self.data = None
        self.l_child = None
        self.r_child = None


class Test:
    def __init__(self):
        self.max_sum = -2 ** 31


    """
    方法功能：求最大子树
    输入参数：root：根节点
    maxRoot最大子树的根节点
    返回值：以root为根节点子树所有节点的和
    """

    def find_max_sub_tree(self, root, maxRoot):
        if root is None:
            return 0
        # 求root左子树所有节点的和
        l_max = self.find_max_sub_tree(root.l_child, maxRoot)
        # 求root右子树所有节点的和
        r_max = self.find_max_sub_tree(root.r_child, maxRoot)
        sums = l_max + r_max + root.data
        # 以root为根的子树的和大于前面求出的最大值
        if sums > self.max_sum:
            self.max_sum = sums
            maxRoot.data = root.data
        # 返回以root为根节点的子树和
        return sums
    """
    方法功能：构造二叉树
    返回值：返回新构造的二叉树
    """
    def construct_tree(self):
        root = BitNode()
        node1 = BitNode()
        node2 = BitNode()
        node3 = BitNode()
        node4 = BitNode()
        root.data = 6
        node1.data = 3
        node2.data = -7
        node3.data = -1
        node4.data = 9
        root.l_child = node1
        root.r_child = node2
        node1.l_child = node3
        node1.r_child = node4
        node2.l_child = node2.r_child = node3.l_child = node3.r_child = node4.l_child = node4.r_child = None
        return root


if __name__ == "__main__":
    # 构造二叉树
    test = Test()
    root = test.construct_tree()
    maxRoot = BitNode()
    test.find_max_sub_tree(root, maxRoot)
    print("最大子树和" + str(test.max_sum))
    print("对应子树的根节点" + str(maxRoot.data))




