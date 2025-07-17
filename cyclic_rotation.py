'''
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
Write a function:
def solution(A, K)
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given
    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]
Given
    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]
'''
def solution(A, K):
    """
    Rotates the array A to the right by K steps
    :param A: List[int] -> The array to be rotated.
    :param K: int -> Number of right rotations.
    :return:  List[int] -> Rotated array.
    """
    N = len(A)
    for i in range(K):
        if N == 0:
            return A
        last_element = A[-1]
        for j in range(N - 1, 0, -1):
            A[j] = A[j - 1]
        A[0] = last_element
    return A

test_cases = [([3, 8, 9, 7, 6], 3),
              ([0, 0, 0], 1),
              ([1, 2, 3, 4], 4),
              ([5, 2, 3, 6, 7, 1], 2),
              ([2, 4, 6, 7], 0),
              ([], 2)
]

for test in test_cases:
    print(solution(*test))




def solution(A, K):
    """
    Rotates the array A to the right by K steps
    :param A: List[int] -> The array to be rotated.
    :param K: int -> Number of right rotations.
    :return:  List[int] -> Rotated array.
    """
    N = len(A)
    if N == 0:
        return A
    K = K % N
    return A[-K:] + A[:-K]

test_cases = [([3, 8, 9, 7, 6], 3),
              ([0, 0, 0], 1),
              ([1, 2, 3, 4], 4),
              ([5, 2, 3, 6, 7, 1], 7),
              ([2, 4, 6, 7], 3),
              ([], 2)
]

for test in test_cases:
    print(solution(*test))