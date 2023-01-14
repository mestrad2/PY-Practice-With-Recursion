# Write code for algorithm 3 below
def nth_fib(n):
    if n <= 0:
        print("Error")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)
    


print("2nd fib number:")
print(nth_fib(2))
print("4th fib number:")
print(nth_fib(4))
print("8th fib number:")
print(nth_fib(8))