# 1)Marks into Grades: A+, A, B, C & D


Marks=int(input("Enter Your Marks: "))
match Marks:
    case m if 95<=m<=100:
        print("Your Grade is A+")
    case m if 85<=m<95:
        print("Your Grade is A")
    case m if 70<m<85:
        print("Your Grade is B")
    case m if 50<m<=70:
        print("Your Grade is C")
    case m if 35<=m<=50:
        print("Your Grade is D")
    case _:
        print("Fail")