# using and 

age = 20
citizen = True
print (age >= 18 and citizen) # true

# using or

is_weekend = False
is_holiday = True
print(is_weekend or is_holiday) # ture

#using not

logged_in = False
print (not logged_in) #true

# if condition

if ( 2==3):
    print("inside if condition")
    print("true")
else:
    print("else condition")

if true:
    print("direct tyue")

a = 10

if false:
    print("direct false")

x = 99
if x > 10:
    print(f"{f} i greater than 10")

percent = 88
if percent >=80 and percent<=100:
    if percent == 100:
        print("topper")
    print("A+")
if percent >=70 and percent<=79:
    print("B+")
if percent >=60 and percent<=69:
    print("C+")
else:
    print("fail")

data = "male" if gender == "m" else "femail"
print (data)

print("-------------------list--------------------")

a = [1,2,3,4,5,6,7,8]
print (a)
print(type(a))

print(a[0])
print(a[1])
print(a[-1])

data = ["ram",1, 7.5, "testing"]
print(data)
print(len(data))

print(len(data)-1)
print(data[4])
