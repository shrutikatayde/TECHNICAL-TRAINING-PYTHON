# N, L = map(int, input().split())
# arr = list(map(int, input(f"Enter age of {N} humans : ").split()[:N]))
# n1 = N // L
# n2 = N % L
#
# print(n1 + n2, "Days")
#
# # or
# # if n1!= 0:
# #     print(n1 + n2, "Days")
# # else:
# #     print(n1, "Days")

# ANOTHER APPROACH
def minimum_days(N, L, ages):
    ages.sort()  # Sort the ages in ascending order
    high_risk_count = 0
    non_high_risk_count = 0
    # Count the number of high-risk and non-high-risk individuals
    for age in ages:
        if age <= 10 or age >= 81:
            high_risk_count += 1
        else:
            non_high_risk_count += 1
    days = 0
    while high_risk_count > 0 or non_high_risk_count > 0:
        capsules = L  # Number of capsules available for the day
        # Distribute capsules to high-risk individuals first
        while capsules > 0 and high_risk_count > 0:
            capsules -= 1
            high_risk_count -= 1
        # Distribute capsules to non-high-risk individuals
        while capsules > 0 and non_high_risk_count > 0:
            capsules -= 1
            non_high_risk_count -= 1
        days += 1
    return days


N, L = map(int, input().split())
ages = list(map(int, input().split()))
result = minimum_days(N, L, ages)
print(result, "Days")
