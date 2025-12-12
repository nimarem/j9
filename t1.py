def my_sum(n):
    if n <= 0:
        return 0
    return n + my_sum(n-1)
my_sum(10)