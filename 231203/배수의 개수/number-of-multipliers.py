cat3=0
cat5=0

for i in range(10):
    num=int(input())
    if num%15==0:
        cat3+=1
        cat5+=1
    elif num%5==0:
        cat5+=1
    elif num%3==0:
        cat3+=1
print(cat3, cat5)