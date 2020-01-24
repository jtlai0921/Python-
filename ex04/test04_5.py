# p_list 是由售價資料庫中取得，程式不會顥示
p_list=[100,500,10000,9800,12000]  #測試資料
for index in range(len(p_list)):
    if p_list[index] >= 10000:
        continue
    p_list[index] = p_list[index] * 0.9 * 1.05
