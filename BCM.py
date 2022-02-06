import pyLIN
import time

ACTIVE_MODE_SLEEP = 0.001
# SLAVE_ADDRESS = 0xC4
SLAVE_ADDRESS = 0x03 # works for BMW

radio_module = pyLIN.LIN('/dev/tty.usbserial-1450',19200)

def scheduleActiveMsg(addr):
    radio_module.sendHeader(addr) 
    response = radio_module.readResponse(9)
    print(response)
    return response

def scheduleMsg(addr, msg):
    # print("{:4x}: {}".format(addr, msg))
    
    radio_module.sendHeader(addr)
    radio_module.sendMessage(msg)
    # time.sleep(0.25)
    response = radio_module.readResponse(9)
    print(response)
    # return response


first_time = True
time_stamp = time.time()
start_time = time_stamp

while True:
    # 10ms loop
    if(time.time() - time_stamp >= ACTIVE_MODE_SLEEP) or first_time==True:

        scheduleActiveMsg(0x03) # polling

        # scheduleDiagMsg2("FF FE A5 FF 30")

        # for x in range(0,0x3c+1):
            # scheduleActiveMsg(x)
            # print(x)
            # scheduleMsg(x, "FF 19 FE FF BC")

        # scheduleMsg(0x05, "00 00 80 00 b8 00 f0 f8 d7")


        # https://linchecksumcalculator.machsystems.cz
        # calc checksum with CAN2.0, enchanced

        # scheduleMsg(0x2B, "FF 00 A5 FF 2f") - no lights
        # scheduleMsg(0x2B, "FF FE A5 FF 30") - works
        # scheduleMsg(0x2B, "FF 0F 91 FF 34") - low lights
        # scheduleMsg(0x2B, "FF FE 19 FF BC") - works !!!
        # scheduleMsg(0x2B, "FF 00 18 FF BC") - no lights

        # if time.time() - start_time > 5:
        #     print('dimming off')
        #     scheduleMsg(0x2B, "FF 00 A5 FF 2f")
        # else:
        #     print('dimming on')
        #     scheduleMsg(0x2B, "FF FE A5 FF 30")

        # scheduleActiveMsg(0x2b)
        # scheduleMsg(0x2B, "FF 19 FE FF 00 00 00 00 BC")

        # scheduleActiveMsg(0x3c)
        # scheduleActiveMsg(0x3d)
        time_stamp = time.time()
        first_time = False

radio_module.close()
print("Done !! ")
