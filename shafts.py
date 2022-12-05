import math as m

Sut=230 #arg from appendix A-22 for Q&T 600ºF treatment of 1045 steel
Sy=220
hp=2.2*1.34 #arg
rpm=9449.0 #arg
bearingspan=4

Kt=1.7 #assume shoulder fillet and assume bending dominates over axial force
Kts=1.5 #assume shoulder fillet
Ma=12*float(input("Enter bending moment in lb ft: ")) #bending moment diagram
Tm= hp/rpm*5252*12 #input from motor

sqrta=[(0.246 -3.08*(10e-3)*Sut + 1.51*(10e-5)*Sut**2 - 2.67*(10e-8)*Sut**3),
   (0.19 -2.51*(10e-3)*Sut + 1.35*(10e-5)*Sut**2 - 2.67*(10e-8)*Sut**3)]
 

# if sqrta[0]>sqrta[1]:
#     actuala=sqrta[0]
# else:
#     actuala=sqrta[1]



Kf=Kt
Kfs=Kts

Seprime=0.5*Sut #assuming Sut is below 200kpsi equation 6-10
ka=2*Sut**(-0.217)  #assume machined shaft
kb=0.9 #assumption
kc=1.0
kd=1.0
ke=1.0

Se=ka*kb*kc*kd*ke*Seprime
n=1.25 #choosing safety factor of 2 ****JUSTIFY???*****

d=(16*n/m.pi*(2*Kf*Ma/Se+(3*(Kfs*Tm)**2)**0.5/Sut))**(1/3)

print("diameter of shaft with a safety factor of 1.25 is: ", d)



d=float(input("Enter small diamter:"))
D=float(input("Enter large diameter:"))
print("D/d is: ", D/d)
r=d/10
print("r/d is: ", r/d)
Kt=float(input("Enter Kt Fig. A-15-9: ")) #(Fig. A–15–9)
Kts=float(input("Enter Kts: Fig. A-15-8: "))#(Fig. A-15-8)

q=1/(1+(sqrta[0])/m.sqrt(r))
qshear=1/(1+(sqrta[1])/m.sqrt(r))

Kf=1+q*(Kt-1)
Kfs=1+qshear*(Kts-1)

Seprime=0.5*Sut #assuming Sut is below 200kpsi equation 6-10
ka=2*Sut**(-0.217)  #assume machined shaft

if d<2:
    kb=(d/0.3)**(-0.107)
else:
    kb=0.91*d**-0.157
kc=1.0 #yields highest safety factor
kd=1.0
ke=0.702

Se=ka*kb*kc*kd*ke*Seprime


#d=(16*n/m.pi*(2*Kf*Ma/Se+(3*(Kfs*Tm)**2)**0.5/Sut))**(1/3)
sigmaAprime=32*Kf*Ma/m.pi/d**3
sigmaMprime=(3*(16*Kfs*Tm/m.pi/d**3)**2)**0.5
n=1/(sigmaAprime/Se+sigmaMprime/Sut)
print("Safety factor with this shaft is: ",n)
ny=Sy/(sigmaAprime+sigmaMprime)
print("Safety Factor with respect to yield strengh: ", ny)

#keyway stress
rd=0.02
r=rd*d
Kt=2.14
Kts=3.0
SutK= 230.0 #304 stainless steel key

sqrta=[(0.246 -3.08*(10e-3)*SutK + 1.51*(10e-5)*SutK**2 - 2.67*(10e-8)*SutK**3),
   (0.19 -2.51*(10e-3)*SutK + 1.35*(10e-5)*SutK**2 - 2.67*(10e-8)*SutK**3)]

q=1/(1+(sqrta[0])/m.sqrt(r))
qshear=1/(1+(sqrta[1])/m.sqrt(r))

Kf=1+q*(Kt-1)
Kfs=1+qshear*(Kts-1)

Seprime=0.5*Sut

ka=2*Sut**(-0.217)  #assume machined shaft

if d<2:
    kb=(d/0.3)**(-0.107)
else:
    kb=0.91*d**-0.157
kc=1.0 #yields highest safety factor
kd=1.0
ke=0.702

Se=ka*kb*kc*kd*ke*Seprime
sigmaAprime=32*Kf*Ma/m.pi/d**3
sigmaMprime=(3*(16*Kfs*Tm/m.pi/d**3)**2)**0.5
nk=1/(sigmaAprime/Se+sigmaMprime/Sut)
print("safety factor of keyway section: ", nk)


#retaining ring

Kt=4.75
Kts=2.75
SutK= 230.0 #304 stainless steel key

sqrta=[(0.246 -3.08*(10e-3)*SutK + 1.51*(10e-5)*SutK**2 - 2.67*(10e-8)*SutK**3),
   (0.19 -2.51*(10e-3)*SutK + 1.35*(10e-5)*SutK**2 - 2.67*(10e-8)*SutK**3)]

q=1/(1+(sqrta[0])/m.sqrt(r))
qshear=1/(1+(sqrta[1])/m.sqrt(r))

Kf=1+q*(Kt-1)
Kfs=1+qshear*(Kts-1)

Seprime=0.5*Sut

ka=2*Sut**(-0.217)  #assume machined shaft

if d<2:
    kb=(d/0.3)**(-0.107)
else:
    kb=0.91*d**-0.157
kc=1.0 #yields highest safety factor
kd=1.0
ke=0.702

Se=ka*kb*kc*kd*ke*Seprime
sigmaAprime=32*Kf*Ma/m.pi/D**3
sigmaMprime=(3*(16*Kfs*Tm/m.pi/D**3)**2)**0.5
nk=1/(sigmaAprime/Se+sigmaMprime/Sut)
print("safety factor of retaining ring section: ", nk)



print("Is critical speed exceeded?")
print((m.pi/bearingspan)**2*m.sqrt(29e6*m.pi/64*d**4/(m.pi*0.25*d**2)/0.284)/2/m.pi*60<rpm)







