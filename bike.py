import math

tfront=46
trear=13
wheel=66
cadance=60
ratio=tfront/trear
speed=ratio*math.pi*wheel*cadance*0.0006
print(ratio)
print(speed)
