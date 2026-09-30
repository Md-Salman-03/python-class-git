#append
data = ["hello",1,2,3,1.5,"testing"]
data.append(2)
data.append(3)

data = []
data.append("broadway")
print(data)

#insert

data = ["hello",1,2,3,]
data.insert(4,100)
data.insert(100,1)
print(data)

#extend

a = [1,2]
b = [3,4]
b.extend(a)
a.extend(b)
print(a)
print(b)

#concat

print("---------------concat------------------")
a = [1,2]
b = [3,4]
c = b+a+a+b
print(a)
print(b)
print(c)

'''
pop
del
clear
remove
'''

#pop
# data = [1,2,3,4,5]
# pop_data = data.pop(1)
# print(data)

# print(pop_data)

# data = []
# data.pop()
# print(data)

# #remove
# data = [1,2,3,4,5,4]
# data.remove(4)
# data.remove(4)

# print(data)

# data.clear()

# '''
# count
# sort
# reverse
# '''

# data = [1,2,3,4,5,9,8,7,6]
# print(data.count(1.5))
# data.reverse()

# data.sort()

# data.sort(reverse=true)
# print(data)

print("----------------------------------------------")

data = [1,2,3,4,5,[4,5,6,7,8,9]]
print(len(data))

print(data[5][3])
print(data[-1][-3])


