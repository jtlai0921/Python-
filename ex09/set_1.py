set1 = {'Anastasia'} 
print(set1)  #{'Anastasia'}
set1 = set('Anastasia')
print(set1)  #{'n', 't', 'i', 'a', 'A', 's'}
set1 = set({'貓':'cat','狗':'dog'})
print(set1)  #{'貓', '狗'}
set1 = set('給我一瓢長江水啊長江水')
print(set1)  #{'水', '長', '瓢', '給', '我', '啊', '江', '一'}
set1.add('酒一樣的長江水')
print(set1)  #{'給', '江', '啊', '瓢', '水', '我', '酒一樣的長江水', '長', '一'}
set1.remove('酒一樣的長江水')
print(set1)  #{'給', '江', '啊', '瓢', '水', '我', '長', '一'}
set1.discard('酒一樣的長江水')
set1.update('酒一樣的長江水')
print(set1) #{'給', '的', '江', '啊', '樣', '瓢', '水', '我', '長', '酒', '一'}
#set1.remove('酒一樣的長江水')
set1.pop()
print(set1) #{'酒', '的', '一', '水', '瓢', '我', '給', '樣', '江', '啊'}
