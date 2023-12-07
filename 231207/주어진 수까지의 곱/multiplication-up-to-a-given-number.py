a, b = map(int, input().split())
su=1

for i in range(a, b+1):
    su*=i
print(su)