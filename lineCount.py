# 统计行数
def line_count(name):
    with open(name, 'r', encoding='UTF-8') as f:
        n = 0
        for line in f:
            n += 1
    return n
