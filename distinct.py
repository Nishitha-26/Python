"""
Write a function
def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.
For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
"""
def solution(A):
    """
    Counts the number of distinct values in the array A.

    :param A: list -> A list of integers.
    :return: int -> An integer representing the count of unique (distinct) values in A.
    """
    if not A:
        return 0
    A.sort()
    distinct_values = 1
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            distinct_values += 1
    return distinct_values
A =  [[2, 1, 1, 2, 3, 1],
      [5, 6, 5, 2, 8, 9],
      []]
for j in A:
    print(f"The number of distinct values is: {solution(j)}")