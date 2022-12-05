shaft_d = float(input("Shaft Diameter (in): "))

if shaft_d = 1.5:
    w1 = 3/8
    h1 = 1/4
    w2 = 3/8
    h2 = w2
    depth = 1/8
else:
    print("Try Again")

T = float(input("Torque (lb in): "))

Force = T/(shaft_d/2)

#Shear

AShear = w1*h1
ShearStress = F/AShear
SF = 2

SYield = 91000 #psi

Ssy = 0.577*SYield

