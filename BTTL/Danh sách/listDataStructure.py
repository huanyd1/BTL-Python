n = int(input("Nhập vào số phần tử của danh sách: "))
a = [0] * n
for i in range(n):
    a[i] = int(input("Nhập vào phần tử của danh sách:"))
print(a[0],end=" , ")
print(a[i])

g = 1
for x in range(i):
    if(a[x] == 13):
        print("Unlucky")
        g = g + 1
        break
    else:
        # print("Lucky") 
        continue
if(g == 1):
    print("Lucky")

medium = (a[0] + a[i])/2
between = int(n / 2)

if(n % 2 == 0):
    print("Số phần tử chẵn")
    # a[between] = medium
else:
    print("Số phần tử lẻ")  
    a[between] = medium 
print(n)
