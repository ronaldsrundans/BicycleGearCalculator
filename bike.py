import math

tfront=42
trear=13
cmwheel=66
rpmcadance=60
ratio=tfront/trear
kmhspeed=ratio*math.pi*cmwheel*rpmcadance*0.0006
print(ratio)
print(kmhspeed)
