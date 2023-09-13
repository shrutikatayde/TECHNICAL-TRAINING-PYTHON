# Input : 021
#         9 4 3 5 7 2 1 9 0 6
# Output : 934

str1 = input()
str1 = list(str1)
arr = list(map(int, input().split()[:10]))

for i in range(len(str1)):
    temp = int(str1[i])
    if temp <= arr[temp]:
        str1[i] = str(arr[temp])

    else:
        break

print("".join(str1))
