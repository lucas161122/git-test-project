def add(x, y):
    return x + y


result = 0

for i in range(11):
    num = add(result, i)
    result = num
print(result)

# terminal will print 55(right number)
