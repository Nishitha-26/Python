"""
An integer N is given, representing the area of some rectangle.
The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.
For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:
def solution(N)
that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.
For example, given an integer N = 30, the function should return 22, as explained above.
"""
def solution(N):
    """
    Finds the minimal perimeter of any rectangle with integer sides and area equal to N.
    :param N: int -> Integer area of the rectangle.
    :return: int -> Minimal perimeter possible with integer side lengths.
    """
    min_peri = []
    A = 1
    while A * A <= N:
        if N % A == 0:
            B = N // A
            perimeter = 2 * (A + B)
            min_peri.append(perimeter)
        A += 1
    return min(min_peri)
print(f"The mimimum perimeter of a rectangle is: {solution(30)}")