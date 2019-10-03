def add_numbers(*numbers):  # "*" mark use to take for different number of arguments
    sum = 0
    for a in numbers:
        sum += a
    print("sum = ", sum)


add_numbers(2, 3)
add_numbers(3)
