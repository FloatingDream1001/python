'''
题目：求1+2!+3!+...+20!的和
'''
sum=0
for i in range(1,21):
    t=1
    for j in range(1,i+1):
        t=t*j
    sum+=t
print(sum)