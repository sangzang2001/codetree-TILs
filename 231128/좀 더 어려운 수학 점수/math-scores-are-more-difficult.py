A=input().split()
B=input().split()

math_A, math_B= int(A[0]), int(B[0])
english_A, english_B= int(A[1]), int(B[1])

if math_A>math_B:
    print('A')
elif math_A==math_B and english_A>english_B:
    print('A')
else:
    print('B')