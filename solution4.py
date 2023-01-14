# Write code for algorithm 4 below
def power(x, y):
    if y < 1:
        print("Error")
    elif y == 1:
        return x
    else:
        return x * power(x, y-1)

print(power(2, 4))