a=int(input())

for i in range(1, a+1):
    s=i//8
    t=i%7
    if i%2==0 and i%4!=0:
        continue
    elif s%2==0:
        continue
    elif t<4:
        continue
    print(i, end=' ')