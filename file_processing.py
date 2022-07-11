# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()

# # Better way to do it.
# with open("fruits.txt") as myfile2:
#     contents = myfile2.read()

# print(content)
# print(contents)

with open("vegetables.txt", "w") as myvegfile:
    myvegfile.write("Tomato\nCucumber\nOnion")
    myvegfile.write("\nGarlic")

# with open("vegetables.txt", "x") as myvegfile:
#     myvegfile.write("\nOkra")
#     # says that file exists, does not append

with open("vegetables.txt", "a") as myvegfile:
    myvegfile.write("\nOkra")

with open("vegetables.txt", "a+") as myvegfile:
    myvegfile.write("\nOkra")
    myvegfile.seek(0)
    content = (myvegfile.read())

print(content)