print ("Введите размерность массива")
N = int (input())
A = [0] * N 
print ("Введите", N,"элементов массива:")
for k in range (N): 
    A[k] = int (input()) 
print (A)


print ("Введите размерность массива")
M = int (input())
B = [0] * M 
print ("Введите", M, "элементов 2 массива:")
for k2 in range(M): 
    B[k2] = int(input()) 

for i in range(len(A)):
    for z in range(len (B)):
        if A[i]==B[i]:
            print ("Общие элементы для обоих массивов:", A[i])