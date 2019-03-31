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
print "calibrating, please rotate the compass in 360 degrees, and keep it horizontal"

for i in range(1,200):
    #print alonzo.read_byte_data( 0x1e,0)
LO
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


print(Xoffset,Yoffset,Zoffset) #check


X_HIGH_BYTE = Xoffset/256
X_LOW_BYTE  = Xoffset%256
Y_HIGH_BYTE = Yoffset/256
Y_LOW_BYTE  = Yoffset%256
Z_HIGH_BYTE = Zoffset/256
Z_LOW_BYTE  = Zoffset%256

print(X_LOW_BYTE+X_HIGH_BYTE*256,Y_LOW_BYTE+Y_HIGH_BYTE*256,Z_LOW_BYTE+Z_HIGH_BYTE*256) #check

alonzo.write_byte_data(0x1c,0x05,X_LOW_BYTE)
alonzo.write_byte_data(0x1c,0x06,X_HIGH_BYTE)
alonzo.write_byte_data(0x1c,0x07,Y_LOW_BYTE)
alonzo.write_byte_data(0x1c,0x08,Y_HIGH_BYTE)
alonzo.write_byte_data(0x1c,0x09,Z_LOW_BYTE)
alonzo.write_byte_data(0x1c,0x0a,Z_HIGH_BYTE)

alonzo.close
