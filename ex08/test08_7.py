name = input('輸入影片名稱：')
score = input('輸入得分：')

print('"{0}",{1}'.format(name, score))
print("\"{0}\",{1}".format(name, score))
print('"%s",%s'%(name, score))
print('"' + name + '",' + score)
print('"{1:s}",{0:s}'.format(score,name))
