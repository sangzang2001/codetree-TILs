A=input().split()
B=input().split()

age_A, age_B= int(A[0]), int(B[0])
sex_A, sex_B= A[1], B[1]

if age_A>=19 and sex_A=='M' or age_B>=19 and sex_B=='M':
    print(1)
else:
    print(0)