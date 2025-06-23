def solution(A):
    min_price = A[0]
    max_profit = 0
    for i in A:
        min_price = min(min_price, i)
        profit = i - min_price
        max_profit = max(max_profit, profit)
    return max_profit

A = [23171, 21011, 21123, 21366, 21013, 21367]
print(solution(A))