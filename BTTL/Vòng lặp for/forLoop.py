#1. Nhập vào số tự nhiên n, in ra n dòng chữ “Hello, Python”.

n = int(input("Nhập vào số tự nhiên n: "))
for i in range(n):
    print("Hello, Python")

#2. Nhập vào số tự nhiên n, in ra n chữ “Python” trên cùng một dòng, 
#cách nhau bởi dấu “-”. 

n = int(input("Nhập vào số tự nhiên n: "))
for i in range(n-1):
    print("Python",end="-")
print("Python")    

#Nhập vào 2 số tự nhiên A và B (A < B). In ra màn hình trên một dòng, cách nhau bởi dấu phẩy:
#1. Các số tự nhiên liên tiếp từ A đến B
#2. Các số lẻ liên tiếp từ A đến B
#3. Các số chẵn liên tiếp, giảm dần từ B đến A

A = int(input("Nhập vào số tự nhiên A: "))
B = int(input("Nhập vào số tự nhiên B: "))
for i in range(A, B, +1):
    print(i, end = " ")
print(B)

if(A % 2 == 0):
    for i in range(A, B, +2):
        print(i, end = " ")
    print(B)
else:
    A = A + 1
    for i in range(A, B, +2):
        print(i, end = " ")
    print(B)    

if(A % 2 != 0):
    for i in range(B, A, -2):
        print(i, end = " ")

else:
    A = A + 1
    for i in range(B, A, -2):
        print(i, end = " ")
    
#4. Nhập vào 1 số tự nhiên n, và n số nguyên, mỗi số trên một dòng. 
#In ra màn hình tổng của n số này.

n = int(input("Nhập vào số tự nhiên n: "))
count = 0
for i in range(n):
    a = int(input("Nhập vào số a tiếp theo: "))
    count = count + a
print("Tổng của",n,"số vừa nhập là: ",count)

#5. Nhập vào số tự nhiên n, tính n giai thừa (n!).

n = int(input("Nhập vào số tự nhiên n: "))
count = 1
for i in range(1 , n+1, 1):
    count = count * i
print("Giai thừa của",n,"là: ",count)      

#6. Viết chương trình nhập vào số nguyên dương N. 
#In ra màn hình họa tiết gồm N dòng như trong ví dụ dưới đây.

n = int(input("Nhập vào số n: "))
for i in range(n+1):
    print((n-i)*" ","*"*i)



