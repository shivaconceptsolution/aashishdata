def fun(*args): #variable length arguments ,
    print(args)
    s=0
    for data in args:
        s=s+data
    print(s)    

fun(10,23,56,67,11,22,8,9,11,23)    

  
