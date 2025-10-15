# Python program to calculate sum of digits of a number

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The sum of digits of {num} is {sum_of_digits(num)}")
