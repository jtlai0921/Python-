g1=['林二','王一','張三','趙六','王一','李四','張三','陳五']
g2=['鄭十','趙六','劉千','廖八','柯七','張三','王一','呂九','柯七','蔡百']
s1 = set(g1)
print('熱門音樂社原來人數：{0}人  正確人數：{1}人'.format(len(g1),len(s1)))
s2 = set(g2)
print('流行音樂社原來人數：{0}人  正確人數：{1}人'.format(len(g2),len(s2)))
s3 =s1.intersection(s2)
print('重複參加社團名單：', s3)
s4 =s1.union(s2)
print('合併後社團人數：{0}人'.format(len(s4)))
