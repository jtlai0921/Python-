def search(member, name):
    for i in range(len(member)):
        if member[i] == name:
            print('已搜尋到', name)
            break
    else:
        print('清單中無', name)
