inp=input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if a>=b:
    if b>=c:
        print(a)
    elif c>=a:
        print(c)
    else:
        pass
elif b>=a:
    if a>=c:
        print(b)
    elif c>=b:
        print(c)
    else:
        pass
else:
    print(c)