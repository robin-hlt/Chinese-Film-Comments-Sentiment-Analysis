import random
f = open('data.txt','r',encoding='utf-8')
lines = f.readlines()
f.close()
random.shuffle(lines)
num = len(lines)
f_train=open('training_set.txt','a',encoding='utf-8')
for item in lines[:int(num*0.8)]:
    f_train.write(item)
f_train.close()
f_test=open('validation_set.txt','a',encoding='utf-8')
for item in lines[int(num*0.8):]:
    f_test.write(item)
f_test.close()