# 统计单词数
import re

def words_count(name):
    with open(name, 'r', encoding='UTF-8') as f:
        n = 0
        for line in f.readlines():
            list_match = re.findall('[a-zA-Z]+', line.lower())
            n += len(list_match)
    return n
