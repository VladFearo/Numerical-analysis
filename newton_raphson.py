# def newton_raphson(a, b, f, f_d, epsilon):
#     m = (a + b) / 2
#     i = 1
#     if f(a) > 0 > f(b) or f(a) < 0 < f(b):
#         while True:
#             temp = m
#             m = m - f(m)/f_d(m)
#             print(f'{i}. {m}')
#             i += 1
#             if abs(temp - m) < epsilon:
#                 return m
#     else:
#         return False
