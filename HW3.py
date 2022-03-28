import random

id_arr = ['315429951','322162553','209202225']

random.shuffle(id_arr)

n = ((int(id_arr[random.randint(0,2)][random.randint(0,2)]) % 4))
if n == 0:
    print("1. linear equations")
elif n == 1:
    print("2. sqrt")
elif n == 2:
    print("3. approximations")
elif n == 3:
    print("4. integrations")


def split(string):
    return [char for char in string]

id = '209202225'
res = 0
id = split(id)
print(id)
for i in id:
    res = int(i) * random.randint(0,9) + res
    #print(res)
while(res > 12):
    res = res % 13
print(res)


