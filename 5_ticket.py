# If there is 'EF' and 'G' in string then remove it from the string

# Input : 1234EF5G
# Output : 12345

ticket = input("Enter the ticket: ")
res = ""
i = 0

while i < len(ticket):
    if ticket[i] == "G":
        i += 1
    elif ticket[i] == "E" and i + 1 < len(ticket) and ticket[i + 1] == "F":
        i += 2
    else:
        res += ticket[i]
        i += 1

print(res)


# Another approach

# str1 = input("Enter the string : ")
# str1 = str1.replace("G", '')
# str1 = str1.replace('EF', '')
# print(str1)






