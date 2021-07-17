#dic={1:2,2:4,3:6,4:8}
#Dic
# n = int(input("Nhập vào số n: "))
# dic={}
# for i in range(1,n+1):
#     dic.update({i:2*i})
# print(dic)

#Câu điều kiện If-else
# a = int(input("Nhập vào số của bạn: "))
# if(a%2 ==0):
#     print("Đây là số chẵn")
# else:
#     print("Đây là số lẻ")

# diem = int(input("Nhập vào điểm của bạn: "))
# if(0<=diem<5):
#     print("Bạn đạt điểm kém")
# elif(5<=diem<6.5):
#     print("Bạn đạt điểm trung bình")
# elif(6.5<=diem<8):
#     print("Bạn đạt điểm khá")
# elif(8<=diem<10):
#     print("Bạn đạt điểm giỏi")
# else:
#     print("Bạn nhập sai định dạng điểm")    

gioitinh = int(input("Nhập vào giới tính (0:Nam - 1:Nữ ):"))
if(gioitinh == 0):
    print("Chào anh đẹp trai!")
elif(gioitinh == 1):
    print("Chào chị xinh gái!")
else:
    print("Cảnh báo : Giới tính không xác định!")
            