"""
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
"""
def solution(A):
    """
    Finds the smallest missing positive integer in a list.
    :param A: list -> List of integers.
    :return: int -> Returns missing integer.
    """
    A.sort()
    small = 1
    for i in A:
        if i == small:
            small += 1
    return small

A = [[1,3,6,4,1,2],
     [1,2,3],
     [-1,-3]]

for j in A:
    print(f"Smallest integer: {solution(j)}")