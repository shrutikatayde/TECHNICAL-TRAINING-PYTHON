# Print the palindrome which holds max length from str1

# input : 'abbdaba'
# output : aba
# explanation --> [a, b, d, bb, aba]

str1 = input()
mx = -656814  # kahi pnn minus value theu shakto

for i in range(len(str1)):
    out = ""
    for j in range(i, len(str1)):
        out += str1[j]

        if out == out[::-1]:
            if mx <= len(out):
                mx = len(out)
                # print(out)

print(mx)
