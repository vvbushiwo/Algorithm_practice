"""
题目描述：给定一趟旅途的全部车票信息，根据这个车票信息找出这趟旅程的路线
如车票：西安-成都，北京-上海，大连-西安，上海-大连
路线为：北京-上海，上海-大连，大连-西安，西安-成都
假设车票无环，即有一个城市只作为终点，而不会作为起点
思路分析：
hash法（python用字典实现）
根据车票信息，建立一个字典
然后从这个字典中找到整个旅程的起点
接着从起点出发依次找到下一站，进而找到终点
（1）根据车票的出发地与目的地构建字典
Tickets={（“西安”到“成都”），（“北京”到“上海”），（“大连”到“西安”），（“上海”到“大连”）}
（2）构建Tickets的逆向字典如下（将旅程的起始点反向）：
ReverseTickets = {（“成都”到“西安”），（“上海”到“北京”），（“西安”到“大连”），（“大连”到“上海”）}
（3）遍历Tickets，对于遍历的key值，判断这个值是否在ReverseTickets中的key中存在，如果不存在，那么说明遍历的Tickets中的key值就是旅途的起点
如果不存在，那么说明遍历的Tickets中的key值就是旅途的起点
"""


def print_result(inputs):
    # 用来存储把input的键与值调换后的信息
    reverse_input = dict()
    for k, v in inputs.items():
        reverse_input[v] = k
    start = None
    # 找到起点
    for k, v in inputs.items():
        if k not in reverse_input:
            start = k
            break
    if start is None:
        print("输入不合理")
        return
    # 从起点出发按照顺序遍历路径
    to = inputs[start]
    print(start + "->" + to)
    start = to
    to = inputs[to]
    while to is not None:
        print("," + start + "->" + to)
        start = to
        to = inputs[to]


if __name__ == "__main__":
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    print_result(inputs)











































