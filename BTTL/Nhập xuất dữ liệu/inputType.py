#2. Viết chương trình nhập vào chiều cao và độ dài cạnh đáy 
# của một tam giác (mỗi số trên một dòng). 
# In ra màn hình diện tích của tam giác đó.

chieuCao = int(input("Nhập vào chiều cao của tam giác: "))
doDaiCanhDay = int(input("Nhập vào độ dài cạnh đáy của tam giác: "))
dienTich = (doDaiCanhDay*chieuCao)/2
print("Diện tích của tam giác là: ",dienTich)

#3. Nhập vào số tự nhiên N. In ra màn hình năm N thuộc thế 
# kỷ thứ mấy. Lưu ý rằng thế kỷ 20 bắt đầu từ năm 1901.
 
N = int(input("Nhập vào năm :"))

if(N % 100 == 0):
    theKy = N/100
else:
    theKy = N//100 + 1
print("Năm ",N,"thuộc thế kỷ",theKy)    

#4. Viết chương trình nhập vào một số tự nhiên N, 
#in ra chữ số tận cùng của nó.

N = int(input("Nhập vào số tự nhiên N: "))
tanCung = N % 10
print("Chữ số tận cùng của",N,"là",tanCung)

#5*. Câu lạc bộ uCode chuẩn bị mua bàn mới cho 03 lớp học, 
# mỗi bàn ngồi được tối đa 02 học sinh. Cho biết số học sinh của mỗi lớp, 
# hãy in ra tổng số bàn ít nhất mà uCode cần trang bị cho 03 lớp học này. 
# Dữ liệu vào gồm số học sinh của 03 lớp, mỗi số trên một dòng. 
# In ra số bàn ít nhất cần trang bị.

soHocSinhLop1 = int(input("Nhập vào số Học sinh lớp thứ nhất: "))
soHocSinhLop2 = int(input("Nhập vào số Học sinh lớp thứ hai: "))
soHocSinhLop3 = int(input("Nhập vào số Học sinh lớp thứ ba: "))

tongSohocsinh = soHocSinhLop1 + soHocSinhLop2 + soHocSinhLop3

soBanCanTrangBi = tongSohocsinh // 2

if(tongSohocsinh % 2 == 0):
    print("Số bàn cần trang bị là: ",soBanCanTrangBi)
else:
    print("Số bàn cần trang bị là: ",soBanCanTrangBi + 1)

#6. Nhập vào một số thực a. In ra màn hình phần thập phân của nó 
# với 3 chữ số thập phân.

a = float(input("Nhập vào số thực a: "))
b = int(a)
x = a - b
print("Phần thập phân của số",a,"(lấy đến 3 chữ số)là: ",round(x, 3))

#7*. Nhập vào một số thực dương a. 
#In ra màn hình chữ số đầu tiên của phần thập phân của số đó.

a = float(input("Nhập vào số thực dương a: "))
a = a*10
a = int(a)
b = a % 10
print("Chữ số đầu tiên của phần thập phân là", b)
