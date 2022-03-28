import random

id = '322162553'
res = 0
id = [char for char in id]
for i in id:
    res += int(i) * random.randint(1, 12)
while res > 12:
    res %= 12
    print('The matrix picked is matrix number: ',res + 19)


