import time
import board
from adafruit_pcf8575 import PCF8575
from adafruit_tca9548a import TCA9548A

# I2C bus 초기화
i2c = board.I2C()

# TCA9548A 각각에 연결된 PCF8575 객체를 생성
tca_addresses = [0x70, 0x71, 0x72, 0x73,0x74]

one_tca = TCA9548A(i2c, tca_addresses[0])
two_tca = TCA9548A(i2c, tca_addresses[1])
three_tca = TCA9548A(i2c, tca_addresses[2])
four_tca = TCA9548A(i2c, tca_addresses[3])
five_tca = TCA9548A(i2c, tca_addresses[4])

one_pcf8575 = PCF8575(one_tca[0])
two_pcf8575 = PCF8575(two_tca[1])
three_pcf8575 = PCF8575(three_tca[2])
four_pcf8575 = PCF8575(four_tca[3])
five_pcf8575 = PCF8575(five_tca[4])

# Green, red pin
Gled_pin = [0, 1, 2, 3, 4, 5, 6, 7]
Rled_pin = [8, 9, 10, 11, 12, 13, 14, 15]

Gled = {}
Rled = {}

# Devices
devices = [one_pcf8575, two_pcf8575, three_pcf8575, four_pcf8575, five_pcf8575]

# Led names
led_names = ['one', 'two', 'three', 'four', 'five']

for i, device in enumerate(devices):
    Gled[led_names[i]] = [device.get_pin(pin) for pin in Gled_pin]
    Rled[led_names[i]] = [device.get_pin(pin) for pin in Rled_pin]

    for pin in Gled_pin + Rled_pin:
        led = device.get_pin(pin)
def common_signal() :
    # Green, red pin
    global Gled_pin
    global Rled_pin

    # Devices
    global devices

    # Led names
    global led_names

    global Gled
    global Rled

    # Declaration
    for i, device in enumerate(devices):
        Gled[led_names[i]] = [device.get_pin(pin) for pin in Gled_pin]
        Rled[led_names[i]] = [device.get_pin(pin) for pin in Rled_pin]

        for pin in Gled_pin + Rled_pin:
            led = device.get_pin(pin)
            #led.switch_to_output(value=True)

    #first pattern
    # 7, 6 green  10,11,12,13,14,15 red

    print('first pattern')
    
    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][7].value = True
        Gled[name][6].value = True

    for name in ['one', 'two', 'three', 'four', 'five']:
        for i in range(2, 8):
            Rled[name][i].value = True

    time.sleep(2)

    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][7].value = False
        Gled[name][6].value = False

        for i in range(2, 8):
            Rled[name][i].value = False

    time.sleep(0)

    #second pattern
    # 5, 4 green 8,9,12,13,14,15 red
    
    print('second pattern')
    
    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][5].value = True
        Gled[name][4].value = True

    for name in ['one', 'two', 'three', 'four', 'five']:
        Rled[name][0].value = True
        Rled[name][1].value = True
        Rled[name][4].value = True
        Rled[name][5].value = True

        if name != 'four':
            Rled[name][6].value = True
            Rled[name][7].value = True

        if name == 'four':
            Rled[name][2].value = True

    time.sleep(2)

    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][5].value = False
        Gled[name][4].value = False

        for i in range(8):
            Rled[name][i].value = False

    time.sleep(0)

    #third pattern
    # 3,2 green 8,9,10,11,14,15 red
    
    print('third pattern')
    
    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][3].value = True
        Gled[name][2].value = True

    for name in ['one', 'two', 'three', 'four', 'five']:
        Rled[name][0].value = True
        Rled[name][1].value = True
        Rled[name][2].value = True
        Rled[name][3].value = True

        if name != 'four':
            Rled[name][6].value = True
            Rled[name][7].value = True

        if name == 'four':
            Rled[name][4].value = True
            Rled[name][5].value = True
            Rled[name][7].value = True

    time.sleep(2)

    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][3].value = False
        Gled[name][2].value = False

        for i in range(8):
            Rled[name][i].value = False

    time.sleep(0)

    #fourth pattern
    # 0,1 green 8,9,10,11,12,13 red

    print('fourth pattern')
    
    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][1].value = True
        Gled[name][0].value = True

    for name in ['one', 'two', 'three', 'four', 'five']:
        Rled[name][0].value = True
        Rled[name][1].value = True
        Rled[name][2].value = True
        Rled[name][3].value = True
        Rled[name][4].value = True
        Rled[name][5].value = True

    time.sleep(2)

    for name in ['one', 'two', 'three', 'four', 'five']:
        Gled[name][1].value = False
        Gled[name][0].value = False

        for i in range(6):
            Rled[name][i].value = False

    time.sleep(0)
