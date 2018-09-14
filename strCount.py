# 统计字符数
def str_count(name):
    with open(name, 'r', encoding='UTF-8') as f:
        n = 0
        for line in f.readlines():
            n += len(line)
    return n
