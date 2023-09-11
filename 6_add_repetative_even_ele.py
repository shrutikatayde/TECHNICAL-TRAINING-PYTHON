# if there are consecutive same charecter are in the string
# but even number of charecter should be present inside this such substring
# we have to add the frequency of that element

# Input : aaabbbaaddcde
# Output : 4

str1 = input("Enter the string : ")
pre = str1[0]
count = 1
sm = 0

for i in range(1, len(str1)):
    if str1[i] == pre:
        count += 1
        # print(str1[i])
    else:
        if count % 2 == 0:
            sm += count

        count = 1
        pre = str1[i]

if count % 2 == 0:
    sm += count


print(sm)






