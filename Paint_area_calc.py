#Paint Area Calculator
import math

def paint_calc(height, width, cover):
    area = height * width
    numb_of_cans = math.ceil(area / cover)
    print(f"You'll need {numb_of_cans} cans of paint, the result have been rounded up.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("How many squaremeters can one can of paint cover?: "))
paint_calc(height=test_h, width=test_w, cover=coverage)
