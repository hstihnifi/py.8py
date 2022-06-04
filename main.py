# 1
# lists are mutable but tuples are immutable

# 2
# in tuples items can't be modified (can't be removed or added ,and replaced within tuples)

# 3
# tuples are immutable

# 4
# ordered

# 5
# a = (1, 2, 3, 4, 5, 6, 7, 8)
# print(a)
# s = _, _, *s, _, _ = a
# print(s)

# 6
# a = (1, 2, 3, 4, 5, 6, 7, 8)
# s = a[3:7]
# print(s)

# 7
# tpl = (7, 10, -3, 18, 6, 10)
# i = list(tpl)
# i[0] = 'x'
# i[5] = 'y'
# tpl = tuple(i)
# print(tpl)

# 8
# def product():

# 9
# def zero_sum(i, index, result):
#     i = (3, 2, -5)
#     result = 0
#     for index in i:
#         result += index
#         if result == 0:
#
#             return True
#         else:
#             return False

# 10
# because it associates a key with an item

# 11
# dict = {"d": }
# print(dict)

# 12
# d['fred'] = 44

# 13 & 14
# A valid key should be present in dictionary or the interpreter generates a
# KeyError exception

# 15
# mutable

# 16
# a)
# {3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
# b)
# 3, 5, 10, 8, 15
# c)
# 3, 5, 10, 8, 15
# d)
# 0, 1, 1, 2, 4

# 17
# ordered(in later versions)

# 18
# from tkinter import Tk, Button
#
# count = 0
#
#
# def update():
#     global count, b
#     count += 1
#     b.configure(text="Click count= " + str(count))
#     print("updating")
#
#
# root = Tk()
# b = Button(root)
# b.configure(background="yellow", text="Click count = 0", command=update)
# b.pack()
# root.mainloop()

# 19

# 20
# In order to use the curly braces for a set, the set must contain at least one element

# 21
# A = set()
# print(type(A))

# 22
# mutable

# 23
# a)
# {2, 19, 20, 7, 10}
# b) True
# c) False
# d) {10,7}
# e) {2, 4, 5, 6, 7, 9, 10, 19, 20}
# f) True
# g) True
# h) False
# i) True
# j) False
# k) 5
# l) {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# m) {0, 5, 8, 17, 18}
# n) {0, 5}
