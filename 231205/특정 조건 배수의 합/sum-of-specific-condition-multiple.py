a, b = map(int, input().split())
su=0
if b>a:
    for i in range(a, b+1):
        if i%5==0:
            su+=i
elif a>b:
    for i in range(b, a+1):
        if i%5==0:
            su+=i

    
print(su)