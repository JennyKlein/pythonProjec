name = input("Enter your name please ")
print("Hello %s, nice to meet you!" % (name))
print("Hello {}, nice to meet you!".format(name))

name = input("Enter your name please ")
age = int(input("How old are you? "))
year_of_birth = 2024 - age

print("Hello %s, nice to meet you! Your year of birth is %d" % (name, year_of_birth))
print("Hello {}, nice to meet you! Your year of birth is {}".format(name, year_of_birth))