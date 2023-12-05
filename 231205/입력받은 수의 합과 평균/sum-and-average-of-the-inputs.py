n=int(input())
su=0

for i in range(n):
    inp=int(input())
    su+=inp
ave=su/n

print(f'{su} {ave:.1f}')