
# random.shuffle(id_arr)
# if int(id_arr[0][0]) in [1,2,3]:
#     random.shuffle(id_arr)
#     if int(id_arr[0][1]) in [1,2,3]:
#         random.shuffle(id_arr)
#     elif int(id_arr[0][1]) in [4, 5, 6]:
#         random.shuffle(id_arr)
#     else:
#         random.shuffle(id_arr)
#         if int(id_arr[0][2]) in [1, 2, 3]:
#             random.shuffle(id_arr)
#         elif int(id_arr[0][2]) in [4, 5, 6]:
#             random.shuffle(id_arr)
#         else:
#             random.shuffle(id_arr)
#
# elif int(id_arr[0][0]) in [4,5,6]:
#     random.shuffle(id_arr)
#     if int(id_arr[0][1]) in [1, 2, 3]:
#         random.shuffle(id_arr)
#     elif int(id_arr[0][1]) in [4, 5, 6]:
#         random.shuffle(id_arr)
#     else:
#         random.shuffle(id_arr)
#         if int(id_arr[0][2]) in [1, 2, 3]:
#             random.shuffle(id_arr)
#         elif int(id_arr[0][2]) in [4, 5, 6]:
#             random.shuffle(id_arr)
#         else:
#             random.shuffle(id_arr)
#
# elif int(id_arr[0][0]) in [7,8,9]:
#     random.shuffle(id_arr)
#     if int(id_arr[0][1]) in [1, 2, 3]:
#         random.shuffle(id_arr)
#     elif int(id_arr[0][1]) in [4, 5, 6]:
#         random.shuffle(id_arr)
#     else:
#         random.shuffle(id_arr)
#         if int(id_arr[0][2]) in [1, 2, 3]:
#             random.shuffle(id_arr)
#         elif int(id_arr[0][2]) in [4, 5, 6]:
#             random.shuffle(id_arr)
#         else:
#             random.shuffle(id_arr)
#
# print(id_arr[0])

# import random
# id_arr = [322162553, 315429951, 209202225]
# random.shuffle(id_arr)
#

#for i in id_arr:
   # n = random.randint(1, 9)
  #  n = i % n
#
# if id_arr[0] % 4 == 0:
#     print("1. linear equations")
# elif id_arr[0] % 4 == 1:
#     print("2. sqrt")
# elif id_arr[0] % 4 == 2:
#     print("3. approximations")
# elif id_arr[0] % 4 == 3:
#     print("4. integrations")
#

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
