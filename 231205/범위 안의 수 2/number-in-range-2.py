su=0
su2=0
for i in range(10):
    inp=int(input())
    if inp>=0 and inp<=200:
        su+=inp
        su2+=1

    
ave=su/su2
print(f'{su} {ave:.1f}')