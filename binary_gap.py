'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
Write a function:
def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
'''
def binary_gap(N):
    """
    Finds the length of the longest sequence of consecutive zeros
    surrounded by ones in the binary representation of a positive integer N.
    :param N: int: takes a positive integer
    :return: int: the length of the longest binary gap
    """
    b = bin(N)[2:]
    max_gap = 0
    current_gap = 0

    for i in b:
        if i == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1

    return max_gap

print(binary_gap(9))
print(binary_gap(32))
print(binary_gap(529))
print(binary_gap(257))
print(bin(9))
print(bin(9)[2:])

def int_to_binary(n):
    """
    Converts a positive integer to its binary string representation
    :param n: int: takes a positive integer
    :return: str: The binary representation of the integer.
    """

    if n == 0:
        return 0
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
print(int_to_binary(9))

def binary_gap(N):
    """
    Finds the length of the longest sequence of consecutive zeros
    surrounded by ones in the binary representation of a positive integer N.
    :param N: int: takes a positive integer
    :return: int: the length of the longest binary gap
    """
    b = int_to_binary(N)
    max_gap = 0
    current_gap = 0

    for i in b:
        if i == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1

    return max_gap

print(binary_gap(9))
print(binary_gap(32))
print(binary_gap(257))


import re
def binary_gap(N):
    """
    Finds the length of the longest sequence of consecutive zeros
    surrounded by ones in the binary representation of a positive integer N.
    :param N: int: takes a positive integer
    :return: int: the length of the longest binary gap
    """
    b = bin(N)[2:]
    binary = re.findall(r'(?<=1)0+(?=1)', b)
    return max(map(len, binary), default=0)
print(binary_gap(9))
print(binary_gap(257))
print(binary_gap(25))
print(binary_gap(32))


def binary_gap(N):
    """
    Finds the length of the longest sequence of consecutive zeros
    surrounded by ones in the binary representation of a positive integer N.
    :param N:int: takes an integer
    :return: int: the length of the longest binary gap
    """
    b = bin(N)[2:]
    gap = b.strip('0').split('1')
    return max(map(len, gap), default=0)

print(binary_gap(9))
print(binary_gap(32))
print(binary_gap(257))


