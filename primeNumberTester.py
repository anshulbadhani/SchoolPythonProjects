num = int(input("Enter a number : "))
half = num / 2
counter = 2

while counter <= half:
    if half % counter == 0:
        print("The number : ", num, " is composite number.")
        break
    else:
        print("The number : ", num, " is a prime number.")
        break
    counter += 1