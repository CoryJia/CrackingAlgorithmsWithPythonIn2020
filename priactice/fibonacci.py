# Python program to display the Fibonacci sequence


# implemented by recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


# implemented by Dynamic Programming
def fibonacci_dp(n):
    res = []

    for i in range(1, n):
        if i == 1:
            res.append(1)
        elif i == 2:
            res.append(1)
        else:
            next_num = res[i - 2] + res[i - 3]
            res.append(next_num)

    return res


if __name__ == '__main__':
    n = int(input("Please enter a positive integer\n"))

    fibo_sequence = []

    for i in range(1, n):
        fibo_sequence.append(fibonacci(i))

    print('fibonacci sequence:')
    print(','.join(str(item) for item in fibo_sequence))

    fibo_sequence = fibonacci_dp(n)
    print('fibonacci sequence:')
    print(','.join(str(item) for item in fibo_sequence))