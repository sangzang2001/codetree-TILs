inp=input().split()
a, b = int(inp[0]), int(inp[1])

for i in range(a, b-1, -1):
    if i%2==0:
        print(i)