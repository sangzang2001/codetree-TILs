a, b = map(int, input().split())
su=0

for i in range(a, b+1):
    if i%2==0:
        su+=i
print(su)