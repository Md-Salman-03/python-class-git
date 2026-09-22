mark = int(input("enter your mark "))
attendance = int(input("enter you attendance"))
if (mark > 100 or mark < 0 ):
    print("invalid mark: enter 0 to 100 ")

elif (mark >= 80 and mark <= 100):
    print("you score is A")
elif (mark >= 70 and mark <= 79 ):
    print ("your score is B")
elif (mark >= 60 and mark <= 69 ):
    print ("your score is c")
elif (mark >= 50 and mark <= 59 ):
    print ("your score is D")
elif (mark <= 50 ):
    print ("you are fail")
    if (attendance <= 75 ):
        print ("your elegible for re-exam")
    else:
        print ("you are not elegible for re-exam")
else:
    print("FAIL")