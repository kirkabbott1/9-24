
# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line
# loop = range(1, 11)
# # # # for number in loop:
# # # #     print number
# # # #
# # # #
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.
# # # loop = range(2, 9)
# # # for stuff in loop:
# # #     print stuff

# Print each odd number between 1 and 10 inclusive.
# # for num in range(1, 11):
# #     if num % 2 != 0:
# #         print num

# Print a square:
# for char in '*****':
#     print char * 5
#
# Print a NxN square of * characters. Prompt the user for N
# N = int(raw_input("How big is the square?"))
# for char in range(0, N):
#     print N * "*"

# Given a height and width, input by the user, print a box consisting of * characters as its border.
#
# h = int(raw_input("height?"))
# w = int(raw_input("width?"))
# for space in range(0, h):
#     if (space == 0) or (space == (h - 1)):
#         print "*" * w
#     else:
#         print "*" + (" " * (w - 2)) + "*"
#
# # Print a Triangle
# print (" " * 2) + ("*" * 3) + (" " * 2)
# print (" ") + ("*" * 5) + (" ")
# # print ("*" * 7)
# nStars = 1
# nBlanks = h + 6
#
# for currentnum in range(0,4):
#     print (" " * (nBlanks / 2)) + ("*" * nStars) + (" " * (nBlanks / 2))
#     nBlanks -= 2
#     nStars += 2

# Print a Triangle II
#
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

# h = int(raw_input("height?"))
#
# #
# # for currentnum in range(0, h):
# #     print (" " * (nBlanks / 2)) + ("*" * nStars) + (" " * (nBlanks / 2))
# #     nBlanks -= 2
# #     nStars += 2
#
# for row_num in range(h):
#     base_w = 2 * h -1
#     num_stars = (row_num * 2) + 1
#     num_spaces = (base_w - num_stars) / 2
#     spaces = " " * num_spaces
#     stars = "*" * num_stars
#     print spaces + stars
# h = int(raw_input("height?"))
length = str(raw_input("width?"))
print length
w = len(length)
print w
for i in range(w):
    if (i == 0):
        print "*" * (w + 2)
    if (i == 1):
        print "*" + (length) + "*"
    if (i == 2):
        print "*" * (w + 2)
        break
