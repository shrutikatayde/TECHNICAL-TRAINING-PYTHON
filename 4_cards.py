# Q. 2 --->> A group of friends playning cards.
# Only numeric cards are being used, alongwith
# the jocker card (equivalent to 0)
# and the symbols in the cards are not taken into account.
# Each player will receive a set of cards.
# The rule of game is to rearrange the set of cards

n = input()
a = []
for i in range(len(n)):
    a.append(int(n[i]))
a.sort()
start =0


# increment the value of start if the 1st element is 0
while start < len(a) and a[start] == 0:
    start += 1

# print the value of 1st non zero element
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













