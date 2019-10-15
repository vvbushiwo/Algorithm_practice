"""
题目描述：
给定一个数组，找出数组中是否有二个数对（a，b）和（c，d），使得a+b=c+d，其中，a、b、c和d是不同的元素
如果有多个答案，打印任意一个即可。
例如给定数组[3，4，7，10，20，9，8]，可以找到二个数对（3，8）和（4，7）使得3+8=4+7
思路：
字典法：以数对为单位进行遍历，遍历过程中，把数对和数对的值存储在字典中（键为数对的和，值为数对）
当遍历到一个键值对时，如果它的和在字典中已经存在，那就找到满足要求的数对
"""


class Pair:
    def __init__(self, first, second):
        self.first = None
        self.second = None
        self.first = first
        self.second = second


def find_pair(arr):
        # 键为数对的和，值为数对
    sumpair = dict()
    n = len(arr)
    # 遍历数组中所有可能的数对
    i = 0
    while i < n:
        j = i + 1
        while j < n:
                # 如果这个数对的和在map中没有，则放入map中
            sums = arr[i] + arr[j]
            if sums not in sumpair:
                sumpair[sums] = Pair(i, j)
            # 如果这个数对的和已经在map中，找出来并打印
            else:
                    # 找出已经遍历过的并存储在map中和为sum的数对
                p = sumpair[sums]
                print("("+str(arr[p.first]) + ", " + str(arr[p.second])+ "), (" + str(arr[i])+", "+str(arr[j])+")")
                return True
            j += 1
        i += 1
    return False


if __name__ == "__main__":
    arr = [3, 4, 7, 10, 20, 9, 8]
    find_pair(arr)
