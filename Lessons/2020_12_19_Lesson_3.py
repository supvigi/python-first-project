# # import openpyxl excel open
# # from openpyxl.styles import Font
# # wb = openpyxl.Workbook()
#
# tuple()
# set()
# dict()
#
# a = {
#     "Детективы": {
#         "Магазин": 12,
#         "Полка": 1,
#         "Места": [1, 2, 3, 4, 5]
#     }
# }
#
#
# def punk_1():
#     x = 10 + 5
#     print(x)
#     return x
#
#
# def punk_2():


x = [1, 2, 3]
y = [6, 5, 4, 5, 8]

if len(x) > len(y):
    for i in range(len(y)):
        x[i] += y[i]
    print(x)
else:
    for i in range(len(x)):
        y[i] += x[i]
    print(y)
