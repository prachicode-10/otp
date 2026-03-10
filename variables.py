n = (input("enter name of student: \n"))
sub1 = int(input("enter marks of sub1\n"))
sub2 = int(input("enter marks of sub2\n"))
sub3 = int(input("enter marks of sub3\n"))
sub4 = int(input("enter marks of sub4\n"))
sub5 = int(input("enter marks of sub5\n"))

avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5
print("u got the grade: ")
if 90< avg<=100:
    print("o")
elif 80< avg<=90:
    print("e")
elif 70 <avg<=80:
    print("a")
elif 60< avg<=70:
    print("b")
elif 50< avg<=60:
    print("c")
else:
    print("fail")




