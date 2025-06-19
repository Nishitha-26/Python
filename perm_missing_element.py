"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
Write a function:
def solution(A)
that, given an array A, returns the value of the missing element.
For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
"""
def solution(A):
    """
    Finds the missing element in an array containing a sequence of distinct integers
    from 1 to N+1, where exactly one element is missing.
    :param A: list -> List of integers containing values from 1 to N+1 with one missing
    :return: int -> The missing integer in the sequence
    """
    N = len(A)
    expect_sum = (N+1) * (N+2) // 2
    actual_sum = sum(A)
    return expect_sum - actual_sum
A = [1,5,2,3]
print(solution(A))
