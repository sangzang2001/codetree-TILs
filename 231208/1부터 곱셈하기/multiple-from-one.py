n=int(input())
su=1

for i in range(1, 11):
    su*=i
    if su>=n:
        print(i)
        break