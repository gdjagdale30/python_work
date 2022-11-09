# #Python Indentation
# for i in range(1,11):
#     print(i)
#     if i==5:
#         break


# #Python Commnts
# #This is a comment

# print("Hello")
# #Multiline Comments
# '''This is multiline comment is perfect example
#     Multiline variable
# '''

# print('This sentence is output to screens')
# # String formatting
# name='Suresh'
# a=45
# b=98

# print("Hello,{}".format(name))
# print(f"Hello,{name}")
# print(f"Hello,{a+b}")

# a,b=10,20
# x=30 if a>b else 40
# print(x)

#Read two numbers 
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

x=a if a>b else b

print(x)