q = input("输入文件目录:")
f = open(q, 'r', encoding="gb18030").read()

#定义转码函数
def encode(s):
    tmp = []
    for c in s:
        tmp.append(bin(ord(c)).replace('0b', ''))
    str_bin = ' '.join(tmp)
    return(str_bin)

b = encode(f)

#存文档
qq = input("输入新文件目录:")
f2 = open(qq,'w')
f2.write(b)