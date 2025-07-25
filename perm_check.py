'''
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
def solution(A)
that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
'''
def solution(A):
    """
    Checks whether the array A is a permutation of numbers from 1 to N
    :param A: List[int] - Input array of integers.
    :return: int - Returns 1 if A is a valid permutation, else 0.
    """
    flag = 1
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            flag = 0
            break
    return flag

testcases = [[1, 2, 4, 3, 5],
             [1, 3, 2, 4],
             [1, 2, 3, 4, 2],
             [1, 2, 5, 3],
             [3, 2, 1],
             [1, 2, 3, 4]]
for j in testcases:
    print(solution(j))

def solution(A):
    """
     Checks whether the array A is a permutation of numbers from 1 to N
    :param A: List[int] - Input array of integers.
    :return: int - Returns 1 if A is a valid permutation, else 0.
    """
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return 0
    return 1
testcases = [[1, 2, 4, 3, 5],
             [1, 3, 2, 4],
             [1, 2, 3, 4, 2],
             [1, 2, 5, 3],
             [3, 2, 1],
             [1, 2, 3, 4]]
for j in testcases:
    print(solution(j))