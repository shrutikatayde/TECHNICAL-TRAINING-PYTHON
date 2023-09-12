# str1 = input()
# arr = []
# for i in range(len(str1)):
#     arr.append(str1[i])
# sarr = arr.sort()
# print(arr)
#
# arr2 = set(sarr)
# print(arr2)


str1 = input()
str2 = input()
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            print(str1[j], end="")
