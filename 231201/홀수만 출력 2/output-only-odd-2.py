inp=input().split()
b, a = int(inp[0]), int(inp[1])

for i in range(b, a-1, -1):
    if i%2==0:
        print(i)