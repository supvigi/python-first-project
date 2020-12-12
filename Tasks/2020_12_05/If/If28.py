year = int(input("Put in the year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("Your year is not leap. It has 365 days")
    else:
        print("Your year is leap. It has 366 days")
else:
    print("Your year is not leap. It has 365 days")
