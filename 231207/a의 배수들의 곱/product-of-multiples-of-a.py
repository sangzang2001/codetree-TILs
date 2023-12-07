a, b = map(int, input().split())
su=1

for i in range(1, b+1):
    if i%a==0:
        su*=i
print(su)