import math

tfront=54
trear=15
cmwheel=66
rpmcadance=60
cad2=90
cad3=120
ratio=tfront/trear
kmhspeed=round(ratio*math.pi*cmwheel*rpmcadance*0.0006, 2)

print("Results(front=",tfront,"t rear=",trear,"t)")
print("Gear ratio:",round(ratio,3))
print("Speed=",kmhspeed,"km/h at cadance of ",rpmcadance ," rpm")
