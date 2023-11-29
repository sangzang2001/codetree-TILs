inp=input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if a>b:
    if b>c:
        print(b)
    elif c>a:
        print(a)
    else:
        print(c)
else: #b>a
    if a>c:
        print(a)
    elif c>b:
        print(b)
    else:
        print(c)