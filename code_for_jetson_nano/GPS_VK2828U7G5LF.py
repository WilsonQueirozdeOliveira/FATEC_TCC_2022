import time
import serial

def main():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         #timeout=3000,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)

    #baud rate
    uart.write
    (b"\xb5\x62\x06\x00\x14\x00\x01\x00\x00\x00\xd0\x08\x00\x00\x80\x25\x00\x00\x07\x00\x07\x00\x00\x00\x00\xa6\xcd\xb5\x62\x06\x00\x01\x00\x01\x08\x22")

    # output frequacy 1hz
    #uart.write(b"\xB5\x62\x06\x08\x06\x00\xE8\x03\x01\x00\x01\x00\x01\x39")
    # output frequacy 0.1hz
    uart.write(b"\xB5\x62\x06\x08\x06\x00\x64\x00\x01\x00\x01\x00\x7A\x12\xB5\x62\x06\x08\x00\x00\x0E\x30")

    #disable others
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x44\x54\x4d\x2a\x33\x42\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x0a\x00\x04\x23") # Disable GPDTM
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x42\x53\x2a\x33\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x09\x00\x03\x21") # Disable GPGBS
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x47\x41\x2a\x32\x37\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x00\x00\xfa\x0f") # Disable GPGGA
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x4c\x4c\x2a\x32\x31\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x01\x00\xfb\x11") # Disable GPGLL
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x52\x53\x2a\x32\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x06\x00\x00\x1b") # Disable GPGRS
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x54\x2a\x32\x36\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x07\x00\x01\x1d") # Disable GPGST
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x56\x2a\x32\x34\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x03\x00\xfd\x15") # Disable GPGSV
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x41\x2a\x33\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x02\x00\xfc\x13") # Disable GPGSA
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x56\x54\x47\x2a\x32\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x05\x00\xff\x19") # Disable GPVTG
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x5a\x44\x41\x2a\x33\x39\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x08\x00\x02\x1f") # Disable GPZDA
    # Turn on the basic GGA and RMC info (what you typically want)
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x52\x4d\x43\x2a\x33\x41\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x04\x01\xff\x18") # Enable GPRMC

    time.sleep(1)

    while True:
        msg = uart.readline().decode('utf-8','ignore')
        if (msg[0] == "$"):
            print(msg)

def init_gps_GPRMC():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         #timeout=3000,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)
    #baud rate
    uart.write (b"\xb5\x62\x06\x00\x14\x00\x01\x00\x00\x00\xd0\x08\x00\x00\x80\x25\x00\x00\x07\x00\x07\x00\x00\x00\x00\xa6\xcd\xb5\x62\x06\x00\x01\x00\x01\x08\x22")

    # output frequacy 1hz
    #uart.write(b"\xB5\x62\x06\x08\x06\x00\xE8\x03\x01\x00\x01\x00\x01\x39")
    # output frequacy 0.1hz
    uart.write(b"\xB5\x62\x06\x08\x06\x00\x64\x00\x01\x00\x01\x00\x7A\x12\xB5\x62\x06\x08\x00\x00\x0E\x30")

    #disable others
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x44\x54\x4d\x2a\x33\x42\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x0a\x00\x04\x23") # Disable GPDTM
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x42\x53\x2a\x33\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x09\x00\x03\x21") # Disable GPGBS
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x47\x41\x2a\x32\x37\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x00\x00\xfa\x0f") # Disable GPGGA
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x4c\x4c\x2a\x32\x31\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x01\x00\xfb\x11") # Disable GPGLL
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x52\x53\x2a\x32\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x06\x00\x00\x1b") # Disable GPGRS
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x54\x2a\x32\x36\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x07\x00\x01\x1d") # Disable GPGST
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x56\x2a\x32\x34\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x03\x00\xfd\x15") # Disable GPGSV
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x41\x2a\x33\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x02\x00\xfc\x13") # Disable GPGSA
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x56\x54\x47\x2a\x32\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x05\x00\xff\x19") # Disable GPVTG
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x5a\x44\x41\x2a\x33\x39\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x08\x00\x02\x1f") # Disable GPZDA
    # Turn on the basic GGA and RMC info (what you typically want)
    uart.write(b"\x24\x45\x49\x47\x50\x51\x2c\x52\x4d\x43\x2a\x33\x41\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x04\x01\xff\x18") # Enable GPRMC
    
def read_gps():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)
    #$GPRMC,060556.00,A,2236.91418,N,11403.24669,E,0.13, 309.62,130214,,,D*7F
    while True:
        try:
            msg = uart.readline().decode('utf-8','ignore')
            if (msg[0:6] == "$GPRMC"):
                data = msg.split(",")
                if data[2] == 'A':
                    #print(msg)
                    return msg#string
                    break
                else:
                    return 0
                    break
        except:
            return 0
            break

def read_latitude():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)
    #$GPRMC,060556.00,A,2236.91418,N,11403.24669,E,0.13, 309.62,130214,,,D*7F
    while True:
        msg = uart.readline().decode('utf-8','ignore')
        if (msg[0:6] == "$GPRMC"):
            data = msg.split(",")
            if data[2] == 'A':
                data_latitude = data[3]
                float_latitude = float(data_latitude)
                degrees = int(float_latitude/100)
                minutes = float_latitude - (degrees*100.0)
                latitude_degrees = degrees + (minutes / 60)
                if data[4] == 'S':
                    latitude_degrees *= -1
                #print("Latitude º:",latitude_degrees)
                return latitude_degrees
                break

def read_longitude():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)
    #$GPRMC,060556.00,A,2236.91418,N,11403.24669,E,0.13, 309.62,130214,,,D*7F
    while True:
        msg = uart.readline().decode('utf-8','ignore')
        if (msg[0:6] == "$GPRMC"):
            data = msg.split(",")
            if data[2] == 'A':
                data_longititude = data[5]
                float_longititude = float(data_longititude)
                degrees = int(float_longititude/100)
                minutes = float_longititude - (degrees*100.0)
                longititude_degrees = degrees + (minutes / 60)
                if data[6] == 'W':
                    longititude_degrees *= -1
                #print("Longitude º:",longititude_degrees)
                return longititude_degrees
                break

def read_velocity():
    uart = serial.Serial(port="/dev/ttyTHS1",
         baudrate=9600,
         bytesize=serial.EIGHTBITS,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,)
    #$GPRMC,060556.00,A,2236.91418,N,11403.24669,E,0.13, 309.62,130214,,,D*7F
    while True:
        msg = uart.readline().decode('utf-8','ignore')
        if (msg[0:6] == "$GPRMC"):
            data = msg.split(",")
            if data[2] == 'A':
                data_velocity = data[7]
                float_velocity = float(data_velocity)
                ms_velocity = float_velocity*0.514444
                #print("Velocity m/s:",ms_velocity)
                return ms_velocity
                break

if __name__ == '__main__':
    main()