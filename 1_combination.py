

# ques. 1

def factorial(n):
    # mCp--> combination logic

    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def pencilEraser(m, n, p, e):

    waysToChoosePencil = factorial(m)//(factorial(p)*factorial(m-p))
    waysToChooseEraser = factorial(n)//(factorial(e)*factorial(n-e))

    totalWays = waysToChoosePencil*waysToChooseEraser
    return totalWays


'''if __name__=="_main__":
    m= int(input("enter number of pencils: "))
    n= int(input("enter number of erasers: "))
    p=int(input("enter number of p: "))
    e=int(input("enter number of e: "))
    result= pencilEraser(m, n, p, e)'''


m = int(input("enter number of pencils: "))
n = int(input("enter number of erasers: "))
p = int(input("enter number of p: "))
e = int(input("enter number of e: "))
res = pencilEraser(m, n, p, e)
print(res)
