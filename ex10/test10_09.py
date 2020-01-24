while True:
    try:
        x = int(input('請輸入一個數字: '))
        break
    except ValueError:
        print('這不是一個有效的數字, 請重新輸入...')