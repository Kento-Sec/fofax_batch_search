label=""
f = open("fofax_search_domain_result.txt",encoding = "utf-8",mode="w")
with open("target.txt",encoding="utf-8",mode="r") as fofa:
    line = fofa.readlines()
    i = 0
    for line_list in line:
        line_new = line_list.replace('\n', '')  # 将换行符替换为空('')
        b = str(label)  # 主要是这一步 将之前列表数据转为str才能加入列表
        line_new = 'domain="' + line_new +'"' + b + '\n'
        i += 1
        print(line_new)
        f.write(line_new)  # 写入一个新文件中
f.close()