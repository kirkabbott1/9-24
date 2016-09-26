# print "string".upper()
# print "STRING".lower()

# # reverse a string
# string = 'Hello'
# output = ''
#
# # for i in range(len(string) -1, -1, -1):
# #     output = output + string(i)
# for char in string:
#     output = (char + output)
# print output
#

# phrase = "lbh zhfg hayrnea jung lbh unir yrnearq"
# print phrase.decode("rot_13")
#
# x = [1,2,3,4,5,6,7]
# print sum(x)
#
# sorted_list = [1,2,3,4,5,6,7,22,23,24]
# odd_numbers = []
#
# for i in sorted_list:
#     if i%2 != 0:
#         odd_numbers.append(i)
# print 'highest number is ', max(odd_numbers)

list1 = [1,23,35,5,6,32,34,36]
# listeven = []
# print min(list1)
# for i in list1:
#     if i%2 == 0:
#         listeven.append(i)
# #     print listeven
# listpos = []
# for i in list1:
#     if i > 0:
#         listpos.append(i)
# print listpos

factorlist = []
for i in list1:
    factorlist.append(i * 2)
print factorlist
