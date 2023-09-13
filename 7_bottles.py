# Input : n = 20
#         r1 = 8
#         r2 = 10
#         r1 = 8
# Output :


def cal(n, r1, r2, r3):
    plastic_b_count = n // r1  # check how many plastic bottles we can buy
    mx = -6416
    if plastic_b_count == 0:
        plastic_b_count += 1

    for i in range(plastic_b_count):
        totalBottles = i
        remaining = n - (i * r1)
        glass_b_count = remaining // r2  # check how many glass bottles we can buy
        totalBottles += glass_b_count
        remaining = (
            remaining % r2
        )  # here remaining amount after if we buy glass bottles

        if glass_b_count != 0:
            remaining += (
                glass_b_count * r3
            )  # return amount after buying the glass bottles

            if remaining < r1 and remaining < r2:
                return (
                    i + glass_b_count
                )  # return if we have less amount-> total bottles-> where i is plastic bottles

            totalBottles += cal(remaining, r1, r2, r3)

        if totalBottles > mx:
            mx = totalBottles

    return mx

    # return i  # if we buy only plastic bottles


n = int(input("Enter total amount : "))
r1 = int(input("Enter amount for plastic bottles : "))
r2 = int(input("Enter amount for glass bottles : "))
r3 = int(input("Enter return amount after buying glass bottles : "))
print(cal(n, r1, r2, r3))

#
# def cal(n, r1, r2, r3):
#     plasticMX = n // r1  # check how many plastic bottles we can buy
#     mxmilk = 0
#     totalBottles = 0
#
#     for i in range(plasticMX + 1):
#         remaining = n - (i * r1)
#         glassbtls = remaining // 2
#         remaining = remaining % r2
#
#         if glassbtls != 0:
#             remaining += glassbtls % r3
#
#             if remaining < r1:
#                 return i + glassbtls
#             totalBottles = max(totalBottles, cal(remaining, r1, r2, r3))
#             return totalBottles
#         return i
#
#
# n = int(input())
# r1 = int(input())
# r2 = int(input())
# r3 = int(input())
#
# print(cal(n, r1, r2, r3))
