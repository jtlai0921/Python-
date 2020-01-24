ulen = 0  #連續大寫字串長度
llen = 0  #連續小寫字串長度
nlen = 0  #交錯字串長度
mlen = 0  #最長交錯字串長度

k = int(input())
str = input()
if (str[0].isupper() == True):
    ulen = 1  #連續大寫字串長度設為1
else:
    llen = 1  #連續小寫字串長度設為1
if k == 1:
    nlen = 1  #交錯字串長度設為1
    mlen = 1  #最長交錯字串長度設為1
for c in str[1:]:
    if (ulen > 0):  #上一個字是大寫
        if(c.isupper() == True):  #連續大寫
            ulen += 1
            if(ulen == k):
                nlen += ulen
                if(nlen > mlen):
                    mlen = nlen
            elif(ulen > k):
                nlen = k
        else:  #由大寫變成小寫
            if(ulen < k):
                nlen = 0
            llen = 1
            ulen = 0
            if(llen == k):
                nlen += llen
                if(nlen > mlen):
                    mlen = nlen
    else:  #上一個字是小寫
        if(c.islower() == True):  # 連續小寫
            llen += 1
            if(llen == k):
                nlen += llen
                if(nlen > mlen):
                    mlen = nlen
            elif(llen > k):
                nlen = k
        else:  #由小寫變成大寫
            if(llen < k):
                nlen = 0
            ulen = 1
            llen = 0
            if(ulen == k):
                nlen += ulen
                if(nlen > mlen):
                    mlen = nlen
print(mlen)
