name="naman abcd xyz aaaaaaa bbbbbbbb sssssssss klmn"

lst=[]
word=""
for i in range(0,len(name)):
    if name[i]==" ":
        lst.append(word)
        word=""
    else:
        word=word+name[i]

lst.append(word)
m=0
mx=''
for i in range(0,len(lst)):
    data =lst[i]
    if(data==data[::-1]):
        if m<len(data):
            m=len(data)
            mx=data
        print(data)

print("Max pallindrom",mx)
        
