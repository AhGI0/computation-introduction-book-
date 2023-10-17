# today we have to made the cube funciton!
# you have to find the write algorithm here!!
def cube(num):
    eplison = .01
    guess = num  / .02
    while abs(guess**3 - num ) > eplison:
        guess = guess - (guess **3 - num ) / (3*guess**2)
    return f'the guess number is {guess}  \n it is the cube for {num}'


Ask = input("Enter a number then i wil give you the cube of it: ")

print(cube(int(Ask)))