inp1=input().split()
inp2=input().split()
inp3=input().split()

ox1, ox2, ox3 = inp1[0], inp2[0], inp3[0]
temp1, temp2, temp3 = int(inp1[1]), int(inp2[1]), int(inp3[1])

if ox1=='Y' and temp1>=37:
    if ox2=='Y' and temp2>=37 or ox3=='Y' and temp3>=37:
        print('E')
    else:
        print('N')
elif ox2=='Y' and temp2>=37:
    if ox3=='Y' and temp3>=37:
        print('E')
    else:
        print('N')
else:
    print('N')