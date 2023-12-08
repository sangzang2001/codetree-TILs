n=int(input())
su=0

for i in range(1, n):
    n/=i
    su+=1
    if n<=1:
        break
    
print(su)