#   FOR SINGLE DIGIT

str1 = input()
n = len(str1)

# lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# sum = 0
# for i in range(n):
#     if str1[i] in list:
#         a = int(str1[i])
#         sum += a
# print(sum)

# FOR GREATER THAN 1 DIGIT

sum1 = 0
prev = str1[0]

for i in range(1, n):
    if str1[i].isdigit():
        if prev.isdigit():
            prev += str1[i]
        else:
            prev = str1[i]
    else:
        if prev.isdigit():
            sum1 += int(prev)
        prev = str1[i]
if prev.isdigit():
    sum1 += int(prev)
print(sum1)
