y = [[1,[2,[3,4,[5,6,[7,8]]]]]]

y1 = y[0][0:1]
print(y1)
y2 = y[0][1:2]
y3 = y2[0][0:1]
print(y3)
y4 = y2[0][1:2]
y5 = y4[0][0:2]
print(y5)
y6 = y4[0][2]
print(y6) #[5,6,[7,8]]
y7 = y6[0:2]
print(y7)
y8 = y6[2]
print(y8)

print(y1+y3+y5+y7+y8)
