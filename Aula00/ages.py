age = int(input("enter your age: "))

if age >= 5 and age <= 7:
    print("you belong to class A")
elif age >= 8 and age <= 10:
    print("you belong to class B")
elif age >= 11 and age <= 13:
    print("you belong to class C")
elif age >= 14 and age <= 17:
    print("you belong to class D")
elif age >= 18:
    print("you belong to class E")
else: 
    print("you are too young to be in school")
