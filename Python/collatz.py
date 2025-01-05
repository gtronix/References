def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

# Main program
if __name__ == "__main__":
    user_input = int(input("Enter number: "))
    while user_input != 1:
        user_input = collatz(user_input)
