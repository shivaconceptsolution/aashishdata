f=1
num = 5
s = ""
for i in range(num,1,-1):  # 1
    s = s + str(i) + "*"
    f=f*i  # 120

print(s,"1=",f)
