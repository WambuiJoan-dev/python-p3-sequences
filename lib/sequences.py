#!/usr/bin/env python3

# With range:

def print_fibonacci(length):

    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    fibonacci_seq = [0, 1]

    while len(fibonacci_seq) < length:
        next_number = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_number)

    print(fibonacci_seq[:length])