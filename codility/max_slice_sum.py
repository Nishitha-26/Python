"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].
Write a function:
def solution(A)
that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
"""
def solution(A):
    """
    Finds the maximum sum of a contiguous subarray
    :param A: list -> A list of integers.
    :return: int -> The maximum sum of any contiguous subarray.
    """
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += A[k]
            res = max(res, sum)
    return res

A = [3, 2, -6, 4, 0]
print(solution(A))


def solution(A):
    """
    Finds the maximum sum of a contiguous subarray
    :param A: list -> A list of integers.
    :return: int -> The maximum sum of any contiguous subarray.
    """
    max_sum = curr_sum = 0
    for i in A:
        max_sum = max(i, max_sum + i)
        curr_sum = max(curr_sum, max_sum)
    return curr_sum
A = [3,2,-6,4,0]
print(solution(A))