# 统计代码行/空行/注释行
def code_count(name):
    with open(name, 'r', encoding='UTF-8') as f:
        code_lines = 0
        comm_lines = 0
        space_lines = 0
        for line in f.readlines():
            if line.strip().startswith('#'):
                comm_lines += 1
            elif line.strip().startswith("'''") or line.strip().startswith('"""'):
                comm_lines += 1
            elif line.count('"""') == 1 or line.count("'''") == 1:
                while True:
                    line = f.readline()
                    comm_lines += 1
                    if ("'''" in line) or ('"""' in line):
                        break
            elif line.strip():
                code_lines += 1
            else:
                space_lines += 1

    return code_lines, comm_lines, space_lines
