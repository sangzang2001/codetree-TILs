y=int(input())

if y%4==0:
    if y%100 and y%400:
        print('true')
    else:
        print('false')
else:
    print('false')