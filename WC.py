import os
import sys
import re
path = 'D:\\'
os.getcwd()
os.chdir(path)

f = open("maoyanDY _1.py", "r", encoding='UTF-8')
#统计行数
def lineCount(f):
    n = 0
    for line in f:

        n = n + 1
    print(n)
    return n
# 统计字符
def strCount():
    f = open("maoyanDY _1.py", "r", encoding='UTF-8')
    n = 0
    for line in f.readlines():
        print(line)
        n += len(line)

    print(n)
    return n
# 统计单词
def wordsCount(f):
    dictResult = {}
    n = 0
    for line in f.readlines():
        listMatch = re.findall('[a-zA-Z]+', line.lower())
        print(listMatch)
        n += len(listMatch)
        for eachLetter in listMatch:
            eachLetterCount = len(re.findall(eachLetter, line.lower()))
            #n += eachLetterCount

            dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount
    print(n)
       # print(listMatch)
    result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)
    #print(result)
    return n
    # for each in result:
    #     print(each)


if __name__ == '__main__':
    a = strCount()
    b = wordsCount(f)
    print(b)
