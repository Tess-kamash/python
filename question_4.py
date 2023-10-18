mark= int(input("Enter your exam marks: "))
if mark >= 70:
    if mark >= 80:
        if mark >=90:
            print("Average grade is: A*")
        else:
            print("Average grade is: A+")
    else:
        print("Average grade is: A")
elif mark >= 60:
    print("Average grade is: B")
elif mark >= 40:
    print("Average grade is: C")
else:
    print("Average grade is: D")

