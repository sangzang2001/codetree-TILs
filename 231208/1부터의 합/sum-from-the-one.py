n=int(input())
su=0

for i in range(1,101):
    su+=i
    if su>=n:
        print(i)
        break