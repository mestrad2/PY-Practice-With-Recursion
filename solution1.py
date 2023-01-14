# Write code for algorithm 1 below
def countdown(number):
    if number == 0:
        return
    else:
        print(number)
        countdown(number - 1)


countdown(9)