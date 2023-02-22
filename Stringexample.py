s1 = "welcome"
c1=0
c2=0
for data in s1:
   if data in ['a','e','i','o','u']:
       c1 = c1+1
   else:
       c2 = c2+1
       


print("Total Vowel is ",c1)
print("Total Consonent is ",c2)
