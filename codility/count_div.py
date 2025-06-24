"""
Write a function:
def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
"""
def solution(A, B, K):
    """
    Counts the number of integers within the range [A-B] that are divisible by K.

    :param A: int -> Start of the range.
    :param B: int -> End of the range.
    :param K: int -> The divisor.
    :return: int -> The number of integers in the range [A-B] divisible by K.
    """
    count = 0
    for i in range(A, B+1):
        if i%K == 0:
            count += 1
    return count


A, B, K = 6, 11, 2
print(solution(A, B, K))