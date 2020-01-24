def progress(a1, d, n):
    an = a1 + (n-1) * d        # 末項
    sn = n * (a1 + an) / 2     # 和
    return an, sn 

a1 = eval(input('輸入數列的首項：'))
d = eval(input('輸入數列的公差：'))
an = eval(input('輸入數列的項數：'))
an, sn = progress(a1, d, an)
print('等差數列的末項為 %d，和為 %d' %(an, sn), end = '')
