import os
import re
# 统计单词数
def words_count(name):
    with open(name, 'r', encoding='UTF-8') as f:
        n = 0
        for line in f.readlines():
            list_match = re.findall('[a-zA-Z]+', line.lower())
            n += len(list_match)
    #       for eachLetter in list_match:
    #           eachLetterCount = len(re.findall(eachLetter, line.lower()))
    #           #n += eachLetterCount
    #
    #           dict_result[eachLetter] = dict_result.get(eachLetter, 0) + eachLetterCount
    #   print(n)
    #       # print(listMatch)
    #   result = sorted(dict_result.items(), key=lambda d: d[1], reverse=True)
    #   #print(result)
    return n
