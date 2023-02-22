age1,age2,age3=23,21,18

res= "age1 is middle" if age1>age2 and age1<age3 or age1<age2 and age1>age3 else   "age2 is middle" if(age2>age1 and age2<age3 or age2<age1 and age2>age3) else "age 3 is middle"

print(res)
