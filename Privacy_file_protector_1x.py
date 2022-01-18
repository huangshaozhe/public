q = input("输入文件目录:")
def decode(s):
    bin_str = ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
    return bin_str

f3 = open(q,'r')
b2 = f3.read()
txt = decode(b2)

#存文档
qq = input("输入新文件目录:")
f4 = open(qq,'w',encoding='gb18030')
f4.write(txt)
