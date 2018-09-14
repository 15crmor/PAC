import os
import sys
from strCount import str_count
from codeCount import code_count
from lineCount import line_count
from wordsCount import words_count
path = 'D:\\'
os.getcwd()
os.chdir(path)
# 遍历文件
def recursive(list):
    f_list = os.listdir(list)
    return f_list

# WC功能
def wc(f, arg):
    if arg[1] == '-c':
        str_num = str_count(f)
        print(f + "文件字符数为: ", str_num)
    elif arg[1] == '-w':
        word_num = words_count(f)
        print(f + "文件单词数为：", word_num)
    elif arg[1] == '-l':
        line_num = line_count(f)
        print(f + "文件行数为：", line_num)
    elif arg[1] == '-a':
        code_lines_num, comm_lines_num, space_lines_num = code_count(f)
        print(f + "文件代码行为：", code_lines_num)
        print("注释行为：", comm_lines_num)
        print("空行为：", space_lines_num)


if __name__ == '__main__':
    args = sys.argv
    if os.path.isfile(args[2]):
        wc(args[2], args)
    elif os.path.isdir(args[2]):
        file_list = recursive(args[2])
        for file in file_list:
            if os.path.splitext(file)[1] == '.py':
                wc(file, args)
    else:
        print("没有此文件，请重新运行此程序")

