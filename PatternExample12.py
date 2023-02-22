ch=65
for i in range(1,6):  #3
    for j in range(1,i+1):  # range(1,4)
        if i%2!=0:  #3%2!=0
            print(chr(ch),end=" ")  # C C C
            
        else:
            print(chr(ch+32),end=" ")  # b b
    ch=ch+1        
    print()        
        
