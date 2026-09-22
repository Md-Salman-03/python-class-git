a = [1,2,3,4,5]
print (a)
a[0]=2
print(a)

#append

a = [1,2,3,4]
a.append("test")
print = 2
a = []
a.append(data)
print(a)

#insert
 
a = [1,2,3,4,5,6]

a.insert(0,100)
a.insert(4,12)

a.insert(10000,2)
print(a)

#extends

a = [1,2,3,4]
b = [1,2,3,4]
b.extend(a)
a.extend(b)
b.extend(b)

print(a)
print(b)

#concat(+)

a = [1,2,4]
b = [5,6,7]

print(a)
c = a+b+b+a+a+a
print(a,b)

print("---------------------"*5)

my_list = [10,20,30,"hello","world","python","nepal"]

del my_list[1]

print(my_list)


#pop

data = my_list.pop(4)
print(my_list)
print(data)

#remove

my_list = [10,20,30,"hello","world","python","nepal"]

my_list.remove(10)

print(my_list)

#clear

my_list.clear()
print(my_list)

a = [1,2,9,8,10,3,4,5,6,6]
print(a.count(6))

print(a.reverse())
a.short()
print(a)
a.short(reverse=true)
print(a)