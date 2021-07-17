# import math
# #Nhập vào một số nguyên n, in ra màn hình giá trị tuyệt đối của n.
# n = int(input("Nhập vào số nguyên n: "))
# print("Giá trị tuyệt đối của",n,"là: ",abs(n))

# #Nhập vào một số nguyên n, kiểm tra n có phải số chẵn không, in ra "YES" hoặc "NO" tương ứng.
# n = int(input("Nhập vào số nguyên n: "))
# if(n % 2 == 0):
#     print("YES")
# else:
#     print("NO")

# #Nhập vào số x, in ra màn hình căn bậc 2 của x nếu x >= 0, nếu không thì báo lỗi "Số âm không có căn bậc 2."

# x = float(input("Nhập vào số nguyên x: "))
# if(0 <= x):
#     print("Căn bậc hai của x là: ",math.sqrt(x))
# else:
#     print("Số âm không có căn bậc 2")    

# #Nhập vào số tự nhiên n, kiểm tra xem n có phải số chẵn có số chữ số khác 2 hay không.
# n = int(input("Nhập vào số tự nhiên n :"))
# if(n % 2 == 0 and n != 2):
#     print("YES")
# else:
#     print("NO") 

# #2. Nhập vào 3 số, kiểm tra xem 3 số có phải 3 cạnh của một tam giác không.

# a = int(input("Nhập vào cạnh thứ nhất của tam giác: "))
# b = int(input("Nhập vào cạnh thứ hai của tam giác: "))
# c = int(input("Nhập vào cạnh thứ ba của tam giác: "))

# if(a + b > c or a + c > b or b + c > a):
#     print("YES")
# else:
#     print("NO")
    
# #3*. Nhập vào số tự nhiên y. Kiểm tra xem năm y có phải là năm nhuận không. 
# y = int(input("Nhập vào năm cần kiểm tra: "))
# if(y % 400):
#     print("Năm ",y,"là năm nhuận")
# else:
#     print("Năm ",y,"không phải là năm nhuận")
# #4*. Nhập vào 3 số, kiểm tra xem 3 số có phải 3 cạnh của một tam giác không. Nếu có, kiểm tra xem tam giác đó là tam giác vuông, tam giác nhọn hay tam giác tù.

# a = int(input("Nhập vào số thứ nhất : "))
# b = int(input("Nhập vào số thứ hai : "))
# c = int(input("Nhập vào số thứ ba : "))

# if(a + b > c or a + c > b or b + c > a):
#     if(a * a == b * b + c * c or b * b == a * a + c * c or c * c == b * b + a * a ):
#         print("Đây là ba cạnh của tam giác vuông")
#     elif(a * a > b * b + c * c or b * b > a * a + c * c or c * c > b * b + a * a):
#         print("Đây là ba cạnh của tam giác tù")
#     else:
#         print("Đây là ba cạnh của tam giác nhọn")        
# else:
#     print("Đây không phải ba cạnh của một tam giác")

#Nhập vào 3 số tự nhiên, in ra màn hình số lớn nhất trong 3 số đó.
# a = int(input("Nhập vào số tự nhiên thứ nhất: "))
# b = int(input("Nhập vào số tự nhiên thứ hai: "))
# c = int(input("Nhập vào số tự nhiên thứ ba: "))

# if(a > b > c or a > c > b):
#     print("Số thứ nhất: ",a,",lớn nhất trong ba số")
# elif(b > a > c or b > c > a):
#     print("Số thứ hai: ",b,",lớn nhất trong ba số")
# else:
#     print("Số thứ ba: ",c,",lớn nhất trong ba số")

#2*. Nhập vào 6 số tự nhiên, in ra màn hình số lớn nhất trong 6 số đó.
print("Nhập vào 6 số không trùng")
a = int(input("Nhập vào số tự nhiên thứ nhất: "))
b = int(input("Nhập vào số tự nhiên thứ hai: "))
c = int(input("Nhập vào số tự nhiên thứ ba: "))
d = int(input("Nhập vào số tự nhiên thứ tư: "))
e = int(input("Nhập vào số tự nhiên thứ năm: "))
f = int(input("Nhập vào số tự nhiên thứ sáu: "))

capLonThuNhat = None
capLonThuHai = None
capLonThuBa = None

if(a > b):
    capLonThuNhat = a
elif(a == b):
    capLonThuNhat = a = b
else:
    capLonThuNhat = b

if(c > d):
    capLonThuHai = c
elif(c == d):
    capLonThuHai = c = d
else:
    capLonThuHai = d

if(e > f):
    capLonThuBa = e
elif(e == f):
    capLonThuBa = e = f
else:
    capLonThuBa = f

if(capLonThuNhat > capLonThuHai > capLonThuBa or capLonThuNhat > capLonThuBa > capLonThuHai):
    print("Số lớn nhất trong 6 số là: ",capLonThuNhat)
elif(capLonThuHai > capLonThuNhat > capLonThuBa or capLonThuHai > capLonThuBa >capLonThuNhat):
    print("Số lớn nhất trong 6 số là: ",capLonThuHai)
else:
    print("Số lớn nhất trong 6 số là: ",capLonThuBa)                                