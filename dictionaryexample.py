stu = {"rno":1001,"sname":"xyz","branch":"cs","fees":45000}
key =[]
value =[]
for k,v in stu.items():
    key.append(k)
    value.append(v)

for i in range(len(value)-1,-1,-1):
    print(key[i],':',value[i])
