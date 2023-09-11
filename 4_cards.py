# Q. 2 --->>
# The rule of game is to rearrange the set of cards in such a way so that the lowest number
# should be made but 1st element should not be zero

# Input : 23890120
# Output : 10022389

n = input("Enter the string : ")

a = []

for i in range(len(n)):
    a.append(int(n[i]))


a.sort()
start = 0

# increment the value of start if the 1st element is 0
while start < len(a) and a[start] == 0:
    start += 1

# print the value of 1st nonzero element
if start != 0:
    print(a[start], end="")


for i in range(len(a)):
    # print all 0's
    if a[i] ==0:
        x=a[i]
        print(x, end="")

    # print remaining elements
    elif a[i]!=a[start]:
        print(a[i], end="")













