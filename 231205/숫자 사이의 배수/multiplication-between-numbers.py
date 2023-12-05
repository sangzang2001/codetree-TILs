a, b = map(int, input().split())
su=0
su2=0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        su+=i
        su2+=1

ave=su/su2
print(f'{su} {ave:.1f}')