import smbus
import math
import time

alonzo = smbus.SMBus(1)

X=[]
Y=[]
Z=[]
#x = alonzo.read_byte_data(0x1e,3)

alonzo.write_byte_data(0x1e,0,0x70) #normal mode (no bias) 8-avg 15hz

alonzo.write_byte_data(0x1e,1,0xa0) #gain 5

alonzo.write_byte_data(0x1e,2,0) #single measurement 1  continous 0

#print(x)

time.sleep(0.006)#steadystate
time.sleep(5)#wait for user
print 'Calibration start, rotate'
#while(1):
for i in range(1,200):
    #print alonzo.read_byte_data( 0x1e,0)

    #print alonzo.read_i2c_block_data( 0x1e,0x03,6)
    

    block =  alonzo.read_i2c_block_data( 0x1e,0x03,6)


    XGUS = block[0]*256+block[1]
    if XGUS > 3267:
        XGUS -= 65535
    ZGUS = block[2]*256+block[3]
    if ZGUS > 3267:
        ZGUS -= 65535
    YGUS = block[4]*256+block[5]
    if YGUS > 3267:
        YGUS -= 65535

    X.append(XGUS)
    Y.append(YGUS)
    Z.append(ZGUS)
    print(XGUS)#,YGUS,ZGUS)

    time.sleep(0.1)


Xoffset=0.5*(max(X)+min(X))
Yoffset=0.5*(max(Y)+min(Y))
Zoffset=0.5*(max(Z)+min(Z))


print(max(X),min(X),Xoffset,max(Y),min(Y),Yoffset)
#print(Xoffset)

while(1):
    block =  alonzo.read_i2c_block_data( 0x1e,0x03,6)

    XGUS = block[0]*256+block[1]
    if XGUS > 3267:
        XGUS -= 65535
    ZGUS = block[2]*256+block[3]
    if ZGUS > 3267:
        ZGUS -= 65535
    YGUS = block[4]*256+block[5]
    if YGUS > 3267:
        YGUS -= 65535


    Xheading=XGUS-Xoffset
    Yheading=YGUS-Yoffset
    Zheading=ZGUS-Zoffset

    theta=math.degrees(math.atan(Yheading/Xheading))
    #print(XGUS,Xoffset,Xheading,theta)#YGUS,ZGUS)
    #print(Xheading,Yheading)#YGUS,ZGUS)

    if Xheading > 0:
        if Yheading > 0:
            print 'NE',theta
        elif Yheading < 0:
            print 'NW',theta+360
        else: #Yheading == 0:
            print 'N',theta
    elif Xheading < 0:
        if Yheading > 0:
            print 'SE',theta+180
        elif Yheading < 0:
            print 'SW',theta+180
        else:
            print 'S',theta

    time.sleep(0.5)

alonzo.close
