def tìm_số_chính_phương(n):
    flag = 0;
    if any (i**2 == n for i in range(n+1)):
        flag = 1
    return flag
n = int(input("nhập một số tự nhiên:"))
check = tìm_số_chính_phương(n);
if check == 1:
    print(n,"là số chinh phương")
else:
    print(n,"không phải là số chính phương")