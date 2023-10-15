# we have to find a way (finding the best way to cube a number!)

#3

def cube ( num):
    espsilon = .01
    guess = num / .02
    while  abs(guess **3 - num >= espsilon):
        guess = guess- (guess**3 - num )/ (3* guess**2)
    print(f'the guess num  of {num} is {guess}')
cube(1957816251)