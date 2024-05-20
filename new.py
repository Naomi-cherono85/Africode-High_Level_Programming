# new_student="Be"
# if new_student== "Dolly Chepkorir":
#     print("the new student is Dolly Chepkorir")
# elif new_student== "Naomi":
#     print("Naomi is not a new student")
# elif new_student== "gladwell":
#     print("gladwell is not a new student")
# elif new_student== "Bett":
#     print("Bett is not a new student")
# else:
#     print(f"{new_student}is not a student")

# age= 17
# height=160
# if age > 18 and height > 170:
#     print("eligible for military services")
# elif age < 18 and height > 170:
#     print("not eligible for military services")
# else:
#     print("other conditions apply")

# is_logged_in= False
# is_admin= False
# if is_logged_in and is_admin:
#     print("admin page")
# elif is_logged_in and not is_admin:
#     print("regular user page")
# else:
#     print("please log in")

# age= 18
# height= 160
# weight=50
# if age > 15 or height >= 160:
#     print("is eligible for military service")
# elif age < 18 or weight >= 50:
#     print("eligible for military service")

# height=170
# is_bribe=True
# if height > 170 or not is_bribe:
#     print("eligible for military service")
# else:
#     print("find another military camp")


# i= 0
# for i in range(2,20,2):
#     print(i)

fruits=["banana", "apple", "orange", "three tomatoes"]
# for fruit in fruits:
#   if fruits== "orange":
#    break
#   print(fruit)
# i=0
# for i, fruit in enumerate(fruits):
#     print(i+1,fruit)

# for i in range(1,20):
#     for x in "abcdef":
#         print(i,x)

# def func_name():
#     print("naomi")
# func_name()

# def sum(num1,num2):
#     if num1 is not int or num2 is not int:
#         return
#     return num1 + num2
# results=sum("8","9")
# print(results)

    
# def multiple_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# multiple_items (first="naomi", last="cherono")

def data_types_infunc(*args):
    print(args)
data_types_infunc ("Ben", {"Language":"Python", "Framework": "Flask", "semester":1}, 3, {"morning lsson", "midday lesson", "afternoon lesson"})