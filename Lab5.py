# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                result += "*"
            else:
                result += " "
            j += 1
        result += "\n"
        i += 1

    return result.rstrip()


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1
        result += "\n"
        i += 1
    
    return result.rstrip()


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1

    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for row in range(1, n +1):
        spaces = " " * (n - row)
        stars = "*" * (1 + 2 * (row - 1))
        result += spaces + stars + "\n"

    return result.rstrip()
