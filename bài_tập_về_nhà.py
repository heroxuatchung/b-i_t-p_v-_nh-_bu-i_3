#BT1
print("tim max min")
def max_min(*numbers):
    print(f"Day duoc truyen vao: {numbers}")
    return max(numbers),min(numbers)
max,min=max_min(3,5,10,1,0,20,30)
print(f"max: {max}, min: {min}")

#BT2
print("Chuoi nghich dao")
def reverse_string(str):
    return str[::-1]
str=input("Nhap chuoi: ")
print(f"Chuoi nghich dao: {reverse_string(str)}")

#BT3
print("Kiem tra so hoan hao")
def is_perfect(n):
    if(n<=0):
        return False
    if sum(i for i in range(1, n//2+1) if n%i==0)==n:
        return True
    else:
        return False
n=int(input("Nhap so muon kiem tra: "))
print(f"{n} la so hoan hao") if is_perfect(n) else print(f"{n} khong la so hoan hao")

#BT4
print("Kiem tra so nguyen to")
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("Nhap so muon kiem tra: "))
if is_prime(n):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong la nguyen to")

#BT5
print("Dem so luong chu hoa, chu thuong")
def count_upper_lower(str):
    upper=lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"So luong chu hoa: {upper}|So luong chu thuong: {lower}")
str=input("Nhap chuoi muon dem: ")
count_upper_lower(str)

#BT6
print("Kiem tra chuoi pangram")
def is_pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str=input("Nhap chuoi muon kiem tra: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
if is_pangram(str,alphabet):
    print(f" \"{str}\" la chuoi pangram")
else:
    print(f" \"{str}\" khong la chuoi pangram")

#BT7
print("Tao ma tran")
def create_matrix(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
n=int(input("Nhap so hang: "))
m=int(input("Nhap so cot: "))
create_matrix(n,m)

#BT8
import math
print("Tinh BMI")
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Beo phi")
    elif bmi >=25:
        print("Thua can")
    elif bmi >=18.5:
        print("Binh thuong")
    else:
        print("Gay")
m=float(input("Nhap can nang: "))
h=float(input("Nhap chieu cao: "))
while m<0 or h<0:
    print("Du lieu khong hop le\n Nhap lai")
    m=float(input("Nhap can nang: "))
    h=float(input("Nhap chieu cao"))
bmi_information(m,h)

#BT9
print("Chuyen hoa thanh thuong va nguoc lai")
def change_upper_lower(str):
    str=str.swapcase()
    print(f"Chuoi sau khi chuyen: {str}")
str=input("Nhap chuoi muon chuyen: ")
change_upper_lower(str)

#BT10
print("De quy dem so luong chu so le")
i=0
def count_odd(n,i):
    if i==len(n) or n[i].isnumeric==False:
        return 0
    if int(n[i])%2!=0:
        return 1+count_odd(n,i+1)
    else:
        return 0+count_odd(n,i+1)

n=input("Nhap so can kiem tra: ")
print(count_odd(n,i))    

#BT11
print("Tim day Fibonacci")
#Tim day Fibonacci theo de quy
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
#Tim day Fibonacci khong de quy
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
n=int(input("Nhap so fibo thu: "))
while n<=0:
    print("So khong hop le\n Nhap lai")
    n=int(input("Nhap so fibo thu: "))
print(f"De quy: {fibo_dequy(n)}")
print(f"Khong de quy: {fibo_thuong(n)}")