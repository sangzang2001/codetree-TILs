su=0
n=int(input())
for i in range(n):
    inp=int(input())
    if inp%2==1 and inp%3==0:
        su+=inp
print(su)