import smbus
import math
import time

alonzo = smbus.SMBus(1)

time.sleep(0.006)#steadystate
time.sleep(3)#wait for user

f=open("calibration.txt",'r')
list=f.readlines()
X=list[0]
Y=list[1]
Z=list[2]
Xoffset=float(X)
Yoffset=float(Y)
Zoffset=float(Z)

print(Xoffset,Yoffset,Zoffset)

def get_heading():


    block =  alonzo.read_i2c_block_data( 0x1c,0x28,6)
    
    XGUS = block[1]*256+block[0]
    if XGUS > 32767:
        XGUS -= 65536
    YGUS = block[3]*256+block[2]
    if YGUS > 32767:
        YGUS -= 65536
    ZGUS = block[5]*256+block[4]
    if ZGUS > 32767:
        ZGUS -= 65536
    
    
    Xheading=XGUS-Xoffset
    Yheading=YGUS-Yoffset
    Zheading=ZGUS-Zoffset
    
    if Xheading == 0:
        Xheading = Xheading+0.00000001
    theta=math.degrees(math.atan(Yheading/Xheading))
    #print(XGUS,Yheading,Xheading,theta,theta1)#YGUS,ZGUS)
    #print(Xheading,Yheading)#YGUS,ZGUS)
    
    if Xheading < 0:
        if Yheading > 0:
            print 'NE',-theta
            return(-theta)
        elif Yheading < 0:
            print 'NW',-theta+360
            return(-theta+360)
        else: #Yheading == 0:
            print 'N',theta
            return(0)
    elif Xheading > 0:
        if Yheading > 0:
            print 'SE',180-theta
            return(180-theta)
        elif Yheading < 0:
            print 'SW',-theta+180
            return(-theta+180)
        else:
            print 'S',theta
            return(180)
    
    #time.sleep(0.5)

alonzo.close
