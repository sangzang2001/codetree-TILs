inp=input().split()
mid, last=int(inp[0]), int(inp[1])

if mid>=90 and last>=95:
    print(100000)
elif mid>=90 and last>=90:
    print(50000)
else:
    print(0)