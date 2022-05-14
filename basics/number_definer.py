number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("Small positive")
    elif number < 1000000:
        print("Large positive")
    else:
        print("Positive")
else:
    if abs(number) < 1:
        print("Small negative")
    elif abs(number) > 1000000:
        print("large negative")
    else:
        print("negative")
