stu = {"stu1":{"rno":101,"name":"xyz"},"stu2":{"rno":102,"name":"abcd"}}

for key in stu:
    print(key,end=' ')
    for dk,dv in stu.get(key).items():
        print(dk,dv,end=' ')
    print()
