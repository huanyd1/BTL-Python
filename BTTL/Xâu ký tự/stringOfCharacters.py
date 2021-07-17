# s1 = str(input("Nhập vào xâu ký tự thứ nhất: "))
# s2 = str(input("Nhập vào xâu ký tự thứ hai: "))

# if(s1 in s2 or s2 in s1):
#     print("YES")
# else:
#     print("NO")    

# s = str(input("Nhập vào xâu ký tự s: "))
# N = int(input("Nhập vào số tự nhiên n: "))

# stringyc = N * s
# print(stringyc*N)

# s1 = str(input("Nhập vào xâu ký tự thứ nhất: "))
# s2 = str(input("Nhập vào xâu ký tự thứ hai: "))
# print(len(s1))
# if(len(s1) == len(s2)):
#     print("=")
# elif(len(s1) > len(s2)):
#     print(">")
# else:
#     print("<")        

s = str(input("Nhập vào xâu ký tự s: "))
N = int(input("Nhập vào số tự nhiên n: "))
if(N > (len(s) - 1)):
    print("Bad Index")    
else:
    print(s[N])
