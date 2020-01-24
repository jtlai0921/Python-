from random import randint
rand = randint(1, 99)
guess = 1
print('猜一個整數，在1～99之間，你可以猜5次')
while (guess <= 5): 
    i =  int(input('你猜多少：'))
    if(i > rand):
        print('再低一點！')
    elif(i < rand):
        print('再高一點！')
    else:
        print('你猜對了！')
        break 
    guess = guess + 1
 
