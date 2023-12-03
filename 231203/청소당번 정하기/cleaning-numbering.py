cat1, cat2, cat3 = 0,0,0
n=int(input())
for i in range(1, n+1):
    if i%12==0:
        cat3+=1
    elif i%3==0:
        cat2+=1
    elif i%2==0:
        cat1+=1
print(cat1, cat2, cat3)