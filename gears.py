import math as m

hp = 1.34*float(input("Input Power (kW): ")) #convert kW to hp

#Geometry - chose available gear from McMaster Carr
dp = float(input("Input Pitch Diameter (in): ")) #4 in
Pd = float(input("Input Diametral Pitch (in):")) #6 in

Np = dp*Pd
Ng = Np #same size gears for simplicilty & 1:1 VR

gamma_lower = m.atan(Np/Ng)
gamma_capital = m.atan(Ng/Np)

face_width = float(input("Input Face Width: ")) #0.86 in
d_av = dp - face_width*m.cos(gamma_capital)

#Force Analysis
rpm = float(input("Input RPM: " )) #8000 motor speed
T = (hp*5252/rpm)*12
w_t = 2*T/d_av

pressure_angle = 20 #20 degrees
w_r = w_t*m.tan(pressure_angle*m.pi/180)*m.cos(gamma_lower)
w_a = w_t*m.tan(pressure_angle*m.pi/180)*m.sin(gamma_lower)

#Strength Analysis
#w_t = 2*T/dp first w_t equation is more accurate

#Gear Contact Stress
C_p = 2290 #for steel
I = float(input("Input I (F15-6 p.800 Shigley): ")) #0.065 Shigley F15-6 p.800
K_o = 1.25 #electric motor input = uniform, propeller = fan = light shock Shigley T15-2 p.797 Mott T9-1 p.378
Q_v = 11 #arb
B = 0.25*((12-Q_v)**(2/3))
A = 50+56*(1-B)
v_t = m.pi*dp*rpm/12
K_v = ((A+m.sqrt(v_t))/A)**B
K_mb = 1 #both members straddle mounted Shigley p.799
K_m = K_mb+0.0036*(face_width**2)
if face_width >= 0.5:
    C_s = 0.5
elif 0.5 <= face_width <= 4.5:
    C_s = 0.125*face_width+0.4375
else:
    C_s = 1

C_xc = 1.5 #properly crowned teeth Shigley p.799

#Contact Stress
sigma_c = C_p*(w_t*K_o*K_v*K_m*C_s*C_xc/(face_width*dp*I))**(1/2)
HBc1 = (sigma_c - 23620)/341

num_flights = 1000
time_flights = 4 
N_L = rpm*time_flights*num_flights
C_L = 3.4822*(N_L**(-0.0602))
C_H = 1 #Since HBp = HBg CH = 1 always
S_H = 1
K_T = 1 #assume t < 250F
C_R = 1 #fail 1 of 100 flights

sigma_c2 = sigma_c*C_L*C_H/(S_H*K_T*C_R)
HBc2 = (sigma_c2 - 23620)/341

if HBc2 - 200 < 10: #test if allowable hardness is close to max 1144 steel hardness
    S_H2 = 200/HBc1
    HBc2Used = 200
else:
    S_H2 = HBc2/HBc1

isShGood = bool(1<S_H2<1.5)

print("\nPinion Parameters:")
print("dp ",dp, "in")
print("Pd ",Pd, "in")
print("Np ",Np, "in")
print("Gamma Lower: ", gamma_lower, "rads")
print("Gamma Capital ",gamma_capital, "rads")
print("Face Width ", face_width, "in")
print("Torque ", T, "lb in")
print("Tangential Force ", w_t, "lb")
print("Radial Force ", w_r, "lb")
print("Axial Force ", w_a, "lb")
print("Contact Stress", sigma_c, "psi")
print('Hardness - Contact Stress ', HBc1, "Brinell")
print("Allowable Contact Stress", sigma_c2, "psi")
print("Hardness - Allowable Contact Stress ", HBc2, "Brinell")
print("Safety Factor", S_H2)
print("Safety Factor is AGMA Acceptable: ", isShGood,"\n")

if 0 < Pd < 16:
    K_s = 0.4867 + 0.2132/Pd
else:
    K_s = 0.5

K_x = 1 #for straight bevel gears

J = float(input("Input J (F15-7 p.800 Shigley): "))

sigma_b = w_t*Pd*K_o*K_v*K_s*K_m/(face_width*K_x*J)
HBb1 = (sigma_b-2100)/44

if 10**2 < N_L < 10**3:
    K_L = 2.7
elif 10**3 < N_L < 3*10**6:
    K_L = 6.1514*N_L**(-0.1192)
elif 3*10**6 < N_L < 10**10:
    K_L = 1.683*N_L**(-0.0323)
else:
    K_L = 1.3558*N_L**(-0.0178)

S_F1 = 1
K_R = C_R

#sigma_b2 = sigma_b*K_L/(S_F1*K_T*K_R)
sigma_b2 = (44*HBc2Used+2100)*K_L/(S_F1*K_T*K_R)
HBb2 = (sigma_b2-2100)/44

if HBb2 < HBc2Used:
    HBb2Used = HBc2Used

S_F2 = HBb2Used/HBb1
isSfGood = bool(S_F2>S_H2 or 0<S_F2<1.5)

print("\nGear 1 Parameters:")
print("dp ",dp, "in")
print("Pd ",Pd, "in")
print("Np ",Np, "in")
print("Gamma Lower: ", gamma_lower, "rads")
print("Gamma Capital ",gamma_capital, "rads")
print("Face Width ", face_width, "in")
print("Torque ", T, "lb in")
print("Tangential Force ", w_t, "lb")
print("Radial Force ", w_r, "lb")
print("Axial Force ", w_a, "lb")
print("Bending Stress", sigma_b, "psi")
print('Hardness - Bending Stress ', HBb1, "Brinell")
print("Allowable Bending Stress", sigma_b2, "psi")
print("Hardness - Allowable Bending Stress ", HBb2, "Brinell")
print("Safety Factor", S_F2)
print("Safety Factor is AGMA Acceptable: ", isSfGood)