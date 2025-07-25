"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.
"""
def solution(A):
    """
     Finds the maximum product of any three integers in the array A.
    :param A: list -> List of integers.
    :return: int -> The maximum possible product of any triplet in A.
    """
    A.sort()
    N = len(A)
    P1 = A[N-1]*A[0]*A[1]
    P2 = A[N-1]*A[N-2]*A[N-3]
    return max(P1,P2)
A=[-3,1,2,-2,5,6]
print(f"The maximum product is: {solution(A)}")

def solution(A):
    """
    Finds the maximum product of any three integers in the array A.
    :param A: list -> List of integers.
    :return: int -> The maximum possible product of any triplet in A.
    """
    A.sort()
    P1 = A[-1]*A[0]*A[1]
    P2 = A[-1]*A[-2]*A[-3]
    return max(P1,P2)
A=[-3,1,2,-2,5,6]
print(f"The maximum product is: {solution(A)}")