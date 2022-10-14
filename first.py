N = int(input("ВВедите размерность массива: "))
B = N * [0]
a=int(input('Как Вы хотите ввести элементы массива? 1 - рандомные значения; 2 - заполнить массив самим (Введите 1 или 2) '))
from random import randint
if a==1:
    for i in range(N):
       B[i]=randint(-100,100)
if a==2:
    for i in range(N): 
        print ("B[", i+1 , "] = ", end="") 
        B[i] = float(input())
print (B)

for i in range(N):
    k = 0 
    while B[i+1] > B[i]:
        i = i+1
        k = k+1
    if B[i+1]<B[i]:
        break
print(B[k])
    


        


