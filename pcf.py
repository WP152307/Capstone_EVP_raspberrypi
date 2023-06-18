import time
import board
from adafruit_pcf8575 import PCF8575
from adafruit_tca9548a import TCA9548A

# I2C bus 초기화
i2c = board.I2C()

# TCA9548A 각각에 연결된 PCF8575 객체를 생성
tca_addresses = [0x70, 0x71, 0x72, 0x73, 0x74]

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


def common_signal():
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
            # led.switch_to_output(value=True)


    print('first pattern')
    first = {
        'one': ([7, 3], [1, 2, 3, 5, 6, 7]),
        'two': ([6, 2], [0, 2, 3, 4, 6, 7]),
        'three': ([4, 1], [0, 1, 2, 4, 5]),
        'four': ([7, 5, 1], [1, 3, 4, 5, 7]),
        'five': ([6, 0], [0, 2, 3, 4, 5, 6])
    }

    for pcf, leds in first.items():
        for led in leds[0]:
            Gled[pcf][led].value = True
        for led in leds[1]:
            Rled[pcf][led].value = True

        time.sleep(2)

        for led in leds[0]:
            Gled[pcf][led].value = False
        for led in leds[1]:
            Rled[pcf][led].value = False

        time.sleep(0)


    print('second pattern')
    second = {
        'one': ([6, 2], [0, 2, 3, 4, 6, 7]),
        'two': ([4, 0], [0, 1, 2, 4, 5, 6]),
        'three': ([5, 3], [0, 1, 3, 5, 6]),
        'four': ([6, 3, 0], [0, 2, 3, 5, 6]),
        'five': ([5, 3], [0, 1, 3, 5, 6, 7])
    }

    for pcf, leds in second.items():
        # Turn on the LEDs
        for led in leds[0]:
            Gled[pcf][led].value = True
        for led in leds[1]:
            Rled[pcf][led].value = True

        time.sleep(2)

        for led in leds[0]:
            Gled[pcf][led].value = False
        for led in leds[1]:
            Rled[pcf][led].value = False

        time.sleep(0)


    print('third pattern')
    states = {
        'one': ([4, 0], [0, 1, 2, 4, 5, 6]),
        'two': ([1, 5], [0, 1, 3, 4, 5, 7]),
        'three': ([7, 2], [1, 2, 3, 4, 6]),
        'four': ([2], [0, 1, 2, 3, 4, 6, 7]),
        'five': ([4, 7, 2], [1, 2, 4, 6, 7])
    }

    for pcf, leds in states.items():
        for led in leds[0]:
            Gled[pcf][led].value = True
        for led in leds[1]:
            Rled[pcf][led].value = True

        time.sleep(2)

        for led in leds[0]:
            Gled[pcf][led].value = False
        for led in leds[1]:
            Rled[pcf][led].value = False

        time.sleep(0)


    print('fourth pattern')
    fourth = {
        'one': ([1, 5], [0, 1, 3, 4, 5, 7]),
        'two': ([7, 3], [1, 2, 3, 5, 6, 7]),
        'three': ([6], [0, 2, 3, 4, 5, 6]),
        'four': ([4], [0, 1, 2, 4, 5, 6, 7]),
        'five': ([1], [0, 1, 2, 3, 4, 5, 7])
    }

    for pcf, leds in fourth.items():
        for led in leds[0]:
            Gled[pcf][led].value = True
        for led in leds[1]:
            Rled[pcf][led].value = True

        time.sleep(2)

        for led in leds[0]:
            Gled[pcf][led].value = False
        for led in leds[1]:
            Rled[pcf][led].value = False

        time.sleep(0)
