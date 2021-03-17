# for i in range(1):
#     print("#", end="")
# print()
# for i in range(2):
#     print("#", end="")
# print()
# for i in range(3):
#     print("#", end="")
# print()
# for i in range(4):
#     print("#", end="")
# print()
# for i in range(5):
#     print("#", end="")
# print()
#
# for i in range(4):
#     for j in range(i+1):
#         print("#", end="")
#     print()

#inverse: when the i value is 0, j will go till 4, when the i value is 1 the value for j will be 3 so it will print 3 #..

# for i in range(4):
#     for j in range(4-i):
#         print("# ", end="")
#     print()
#
# for i in range(4):
#     for j in range(1+i):
#         print("#",end="")
#     print("  ", end="")
#     for j in range(i+1):
#         print("#", end="")
#
#
#     print()




while True:
    n = int(input("Height: "))
    if n >= 1 and n <= 8:
        break
for i in range(n):
    print(" " * (n - 1 - i), end="")
    print("#" * (i + 1), end="")
    print(" " * 2, end="")
    print("#" * (i + 1), end="")
    print()

