def prime_Checker(number):
    if number == 1:
        return False, []
    else:
        factors = []
        for i in range(2, number):
            if number % i == 0:
                factors.append(i)

        if len(factors) == 0:
            return True, []
        else:
            return False, factors


def main():
    numbers = [int(x) for x in input("Enter a range (seperated by comma, e.g. \" 5,10 \"): ").split(",")]
    for number in range(numbers[0], numbers[1]+1):
        is_Prime, factors = prime_Checker(number)
        if number == 1:
            continue
        if not is_Prime:
            print("Factors for "+ str(number) + " are: " + str(factors))
        else:
            print(str(number) + " is Prime!")

if __name__ == '__main__':
    main()
