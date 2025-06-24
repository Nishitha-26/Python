"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.
Write a function:
def solution(X, Y, D)
that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
"""
def solution(X, Y, D):
    """
    Calculates the minimal number of jumps required for a position X to reach
    or exceed position Y, jumping a fixed distance D each time.
    :param X: int -> Starting position
    :param Y: int -> Target position
    :param D: int -> Fixed jump distance
    :return:  int-> Minimum number of jumps needed to reach or pass Y
    """
    jumps = 0
    while X < Y:
        X += D
        jumps += 1
    return jumps


test_cases = ((10, 85, 30),
              (20, 100, 20),
              (5, 40, 10))

for test in test_cases:
    print(solution(*test))

