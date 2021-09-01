## 普通的FIFO 队列式分支限界法
## 当 不满足总价格不超过d的要求时，则剪枝
## 当搜索到深度n时，即搜索到了叶节点，不再进行扩展节点的操作，而是针对于叶节点所对应的最小值，
# 反向求得该节点所对应的的路径

# 加入优先级--使用当前节点的重量作为优先级，重量小优先级高
# 将队列改成列表，以append的方式加入到列表中，再以排序的方式维护当前列表的首个元素为最小权值

# coding : utf-8


# 得到当前扩展节点所在的Level
def getlevel(m, currrent):
    i = 1
    level = 0
    sum = 0
    if currrent == 0:
        level = 0
        return level
    while (1):
        level = level + 1
        sum = m ** level + sum  # sum=m
        if sum - m ** level < currrent <= sum:  # m-m^0 = m-1
            return level


# 得到当前扩展节点，所对应的首个子节点所在的索引
def get_idx(m, current):
    level = getlevel(m, current)
    # 求current 在该level中的相对索引，即 相对于该level第一个元素的位置
    current_level_idx = current - sum([m ** i for i in range(level)])
    # 子节点所在层的开始绝对索引
    start_idx = sum([m ** i for i in range(level + 1)])

    return start_idx + current_level_idx * m


# 得到最优解之后，反向查找其路径
def get_path(m, current):
    path = []
    path.append(current % m)  # from 1, not from 0

    while 1:
        level = getlevel(m, current)
        if level == 1:
            return path[::-1]
        current_level_idx = current - sum(
            [m ** i for i in range(level)])  # # 求current 在该level中的相对索引，即 相对于该level第一个元素的位置
        path.append(current_level_idx // m + 1)  # 得到上一级的索引位置
        current = sum([m ** i for i in range(level - 1)]) + current_level_idx // m  # 得到上一级的值


# 为活结点表中的节点 定义了一个类
class Node:
    def __init__(self, idx, weight):
        self.idx = idx
        self.weight = weight


def MinWighet(n, m, d, price, weight):
    # 子集树中的节点数
    vec_len = sum([m ** i for i in range(1, n + 1)]) + 1
    que = []
    que.append(Node(0, 0))  # 在活结点表中加入根节点
    # vec_price = [0 for _ in range(vec_len)]
    # vec_weight = [0 for _ in range(vec_len)]

    while (que):  # 当活结点表非空时
        que = sorted(que, key=lambda node: node.weight)  # 类似于最小堆的维护
        current = que[0]  # 得到当前扩展节点（索引号）
        level = getlevel(m, current.idx)  # 当前 扩展节点所在的level

        new_node_idx = get_idx(m, current.idx)  # 得到当前扩展节点，所对应的首个子节点所在的索引

        # 若搜索完了整棵树
        if getlevel(m, current.idx) == getlevel(m, vec_len) - 1:
            minweight = current.weight
            min_at_idx = current.idx

            path = get_path(m, min_at_idx)
            return minweight, path

        # 判断当前的扩展结点下的所有子节点是否可以加入活结点队列中
        for i in range(m):
            if int(current.weight + price[level][i]) <= d:
                new_node = Node(new_node_idx, int(current.weight + weight[level][i]))
                que.append(new_node)
            new_node_idx += 1

        # 将当前的扩展节点失活
        del que[0]


if __name__ == '__main__':
    n = 3
    m = 3
    d = 4

    price = [[1, 2, 3], [3, 2, 1], [2, 2, 2]]
    weight = [[1, 2, 3], [3, 2, 1], [2, 2, 2]]
    result = MinWighet(n, m, d, price, weight)
    print(MinWighet(n, m, d, price, weight))
