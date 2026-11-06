
name = input("Enter student name: ")

math = int(input("Enter Math marks: "))

english = int(input("Enter English marks: "))

python= int(input("Enter Python marks: "))


if math < 0 or math > 100:
    print("invalid marks")

elif english < 0 or english > 100:
    print("invalid marks")

elif python < 0 or python > 100:
    print("invalid marks")

else:
    avarage =(math + english +python)/3


if ( 80 <= avarage ):
    final_grade = "A+"

elif ( 70 <= avarage):
    final_grade = "A"

elif ( 60 <= avarage ):
    final_grade = "A-"

elif ( 50 <= avarage ):
    final_grade = "B"

elif ( 40 <= avarage ):
    final_grade = "C"

else:
    final_grade = "F"

print(f"Student Name: {name}")
print(f"Avarage Markes: {avarage}")
print(f"Final Grade: {final_grade}")
