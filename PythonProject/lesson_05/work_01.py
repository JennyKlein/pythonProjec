
name = input("Enter your name please!")
print("Hello, my name is ", name)

city = input("Where are you from?")
print("%s is a beautiful place!" % (city))

age = input("How old are you? ")
int_age = int(age)
year_of_birth = 2024 - int_age
print ("Your year of birth is %d" %(year_of_birth))

height = float(input("How tall are you? Please enter answer in m"))
height_in_foot = height / 0.3

print ("Your height in foots is %.2f!" % (height_in_foot))