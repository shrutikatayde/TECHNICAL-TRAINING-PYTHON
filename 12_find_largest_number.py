arr = list(input("Enter the array:"))
arr.sort()
a = arr[::-1]
rev_str = "".join(a)
print(rev_str)

# for integer conversion of int number to integer digit
# suppose  --> input = 9872
# 9*10 = 90 --> 90+8 = 98 --> 98*10 = 980 --> 980+7 = 987 --> 987*10 --> 9870 +2 = 9872
