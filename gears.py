import math as m

hp = 2.4*1.34

#Geometry
dp = 4
Pd = 6 #arb

Np = dp*Pd
Ng = Np

gamma_lower = m.atan(Np/Ng)
gamma_capital = m.atan(Ng/Np)

face_width = 0.86 
d_av = dp - face_width*m.cos(gamma_capital)

#Force Analysis
rpm = 8000
T = (hp*5252/rpm)*12
w_t = 2*T/d_av

pressure_angle = 20
w_r = w_t*m.tan(pressure_angle*m.pi/180)*m.cos(gamma_lower)

w_a = w_t*m.tan(pressure_angle*m.pi/180)*m.sin(gamma_lower)

#Strength Analysis
w_t = 2*T/dp

#Gear Contact Stress
C_p = 2290 #for steel
I = 0.065 #Shigley F15-6 p.800
K_o = 1.25 #electric motor input = uniform, propeller = fan = light shock Shigley T15-2 p.797 Mott T9-1 p.378
Q_v = 7 #arb
B = 0.25*(12-Q_v)**(2/3)
A = 50+56*(1-B)
v_t = m.pi*dp*Np/12
K_v = ((A+m.sqrt(v_t))/B)**B
K_mb = 1 #both members straddle mounted Shigley p.779
K_m = K_mb+0.0036*face_width**2
if face_width >= 0.5:
    C_s = 0.5
elif 0.5 <= face_width <= 4.5:
    C_s = 0.125*face_width+0.4375
else:
    C_s = 1

C_xc = 1.5 #properly crowned teeth Shigley p.799

#Contact Stress
sigma_c = C_p*(w_t*K_o*K_v*K_m*C_s*C_xc/(face_width*dp*I))**(1/2)

HB1 = (sigma_c - 23620)/341
num_flights = 100
time_flights = 4 
N_L = rpm*time_flights*num_flights
C_L = 3.4822*N_L**(-0.0602)
C_H = 1 #FOR PINION ONLY
S_H = 1
K_T = 1 #assume t < 250F
C_R = 1 #fail 1 of 100 flights

sigma_c2 = sigma_c*C_L*C_H/(S_H*K_T*C_R)

HB2 = (sigma_c2 - 23620)/341

#NEED TO FIND MATERIALS AND CALCULATE SF BASED ON THAT

print("dp ",dp)
print("Pd ",Pd)
print("Np ",Np)
print("Gamma Lower: ", gamma_lower)
print("Gamma Capital ",gamma_capital)
print("Face Width ", face_width)
print("Torque ", T)
print("Tangential Force ", w_t)
print("Radial Force ", w_r)
print("Axial Force ", w_a)
print("Contact Stress", sigma_c)
print('Hardness - Contact Stress ', HB1)
print("Allowable Contact Stress", sigma_c2)
print('Hardness - Allowable Contact Stress ', HB2)