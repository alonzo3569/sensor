import smbus
import math
import time

alonzo = smbus.SMBus(1)

X=[]
Y=[]
Z=[]
#x = alonzo.read_byte_data(0x1e,3)

alonzo.write_byte_data(0x1c,0x20,0x7c) #ultra mode odr 80hz

alonzo.write_byte_data(0x1c,0x21,0x20) #fullscale 8g

alonzo.write_byte_data(0x1c,0x22,0x00) #continous conversion mode

#print(x)

time.sleep(0.006)#steadystate
time.sleep(3)#wait for user

#while(1):
for i in range(1,200):
    #print alonzo.read_byte_data( 0x1e,0)

    #print alonzo.read_i2c_block_data( 0x1e,0x03,6)
    

    block =  alonzo.read_i2c_block_data( 0x1c,0x028,6)


    XGUS = block[1]*256+block[0]
    if XGUS > 32767:
        XGUS -= 65536
    YGUS = block[3]*256+block[2]
    if YGUS > 32767:
        YGUS -= 65536
    ZGUS = block[5]*256+block[4]
    if ZGUS > 32767:
        ZGUS -= 65536

    X.append(XGUS)
    Y.append(YGUS)
    Z.append(ZGUS)
    print(XGUS,YGUS,ZGUS)

    time.sleep(0.1)


Xoffset=0.5*(max(X)+min(X))
Yoffset=0.5*(max(Y)+min(Y))
Zoffset=0.5*(max(Z)+min(Z))


print(max(X),min(X),Xoffset,max(Y),min(Y),Yoffset)
#print(Xoffset)

while(1):
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
    float(Xheading)
    float(Yheading)
    float(Zheading)

    if Xheading == 0:
        Xheading = Xheading+0.00000001
    theta=math.degrees(math.atan(Yheading/Xheading))
    theta1=math.degrees(math.atan2(Yheading,Xheading))
    #print(XGUS,Yheading,Xheading,theta,theta1)#YGUS,ZGUS)
    #print(Xheading,Yheading)#YGUS,ZGUS)

    if Xheading < 0:
        if Yheading > 0:
            print 'NE',-theta
        elif Yheading < 0:
            print 'NW',-theta+360
        else: #Yheading == 0:
            print 'N',theta
    elif Xheading > 0:
        if Yheading > 0:
            print 'SE',180-theta
        elif Yheading < 0:
            print 'SW',-theta+180
        else:
            print 'S',theta

    #time.sleep(0.5)

alonzo.close
