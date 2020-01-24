def triangle(B = 6, H = 6):
    print()
    print('三角形的底為%d, 高為%d' %(B, H))
    A = B * H / 2
    return A

area1 = triangle()
print('三角形的面積為 %d' %area1)
base = 10
area2 = triangle(base)
print('三角形的面積為 %d' %area2)
base = 10
high = 5
area3 = triangle(base, high)
print('三角形的面積為 %d' %area3)
