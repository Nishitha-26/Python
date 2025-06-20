"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).
Write a function:
def solution(N)
that, given a positive integer N, returns the number of its factors.
For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.
"""
def solution(N):
    """
    Counts the number of positive divisors of the integer N.
    :param N: int -> Integer to find the number of positive divisors for.
    :return: int -> Total number of positive divisors.
    """
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
        i += 1
    return count

A = 24
print(f"The number of factors are: {solution(A)}")