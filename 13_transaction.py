# Q. 10


def is_transaction(arr, n_of_customer):
    # Shopkeeper wallet
    collect_thirty = 0
    collect_sixty = 0
    collect_one_twenty = 0
    # Shopkeeper wallet end

    for i in range(n_of_customer):
        if arr[i] == 30:
            collect_thirty += 30
        elif arr[i] == 60:
            # we have to return 30 if possible
            if collect_thirty >= 30:
                collect_thirty -= 30  # return 30 if we give 60
                collect_sixty += 60  # add to wallet for 60
            else:
                return False

        elif arr[i] == 120:
            if collect_thirty >= 90:
                collect_thirty -= 90  # return 90 if we give 120
                collect_one_twenty += 120  # add to wallet for 120
            elif collect_thirty >= 30 and collect_sixty >= 60:
                collect_thirty -= 30  # return 30 if we give 120
                collect_sixty -= 60  # return 60 if we give 120
                collect_one_twenty += 120
            else:
                return False

    return True


shopkeeper_wallet = 0
n_of_customer = int(input("Enter no. of customer : "))
arr = []
for i in range(n_of_customer):
    arr.append(int(input("Enter the amount of all items you buy : ")))
result = is_transaction(arr, n_of_customer)
if result:
    print("Transaction successful")
else:
    print("Transaction failed")
