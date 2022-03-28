import random
id_arr = ['315429951']


n = (int(id_arr[0][random.randint(0, 8)]) * int(id_arr[0][random.randint(0, 8)]) % 12) + 19
print("question number:", n)