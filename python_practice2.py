
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
# print ("*" * 7)
nStars = 1
nBlanks = 6

counter = 1
for space in range(0,4):
    print (" " * (nBlanks / 2)) + ("*" * nStars) + (" " * (nBlanks / 2))
    counter += 1
    if counter > 0:
        nBlanks -= 2
        nStars += 2
